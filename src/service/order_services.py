import os
from src.repository import order_repository
from src.service import user_services, bouquet_services
from src.database.models import Order, OrderBouquets, OrderHistory
from fastapi import HTTPException, status
from config import Config
from src.utils.custom_logging import setup_logging
config = Config()
log = setup_logging()


async def get_all_orders():
    orders = order_repository.get_all_orders()
    return [Order(**order) for order in orders]


async def get_order_by_id(order_id: int):
    order = order_repository.get_order_by_id(order_id)
    return Order(**order) if order else None


async def get_orderbouquets_by_order_id(order_id: int):
    orderbouquets = order_repository.get_orderbouquets_by_order_id(order_id)
    return [OrderBouquets(**orderbouquet) for orderbouquet in orderbouquets]


async def get_order_by_user_id(user_id: int):
    orders = order_repository.get_order_by_user_id(user_id)
    return [Order(**order) for order in orders]


async def create_order(order: Order):
    order_id = order_repository.create_order(order)
    return await get_order_by_id(order_id)


async def create_orderbouquets(orderbouquets: OrderBouquets):
    order_id = order_repository.create_orderbouquets(orderbouquets)
    return await get_order_by_id(order_id)


async def update_order(order_id: int, order: Order):
    order_repository.update_order(order_id, order)
    return {"message": "Order updated successfully"}


async def delete_order(order_id: int):
    order_repository.delete_order(order_id)
    return {"message": "Order deleted successfully"}


async def buy_history_order(user_id: int):
    # Проверяем существоние пользователя
    user = await user_services.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    # Получаем заказы пользователя
    orders = await get_order_by_user_id(user_id)
    history = []
    # Проходим по всем заказам
    for order in orders:
        # Получаем информацию о букетах и их количестве для заказа
        orderbouquets = await get_orderbouquets_by_order_id(order.ID)
        # Создаем и записываем в модель историю заказа
        orderhistory = OrderHistory(order_id=order.ID,
                                    user_id=order.UserID,
                                    date=order.Date,
                                    total_price=order.TotalPrice,
                                    bouquets=orderbouquets)
        # Добавляем историю заказа в список
        history.append(orderhistory)
    return history


async def buy_create_order(user_id, bouquetsID, off_bonus):
    # Проверяем существоание пользователя
    user = await user_services.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not exist")
    bouquets = []
    total_price = 0
    # Проходим по каждому букету в переданном листе.
    for bouquetID in bouquetsID:
        # Проверяем существование букета
        bouquet = await bouquet_services.get_bouquet_by_id(bouquetID.BouquetID)
        if not bouquet:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bouquet not exist")
        # Сохраняем информацию о букете
        price = bouquet.Price
        quantity = bouquetID.Quantity
        # Если передано нулевое количество букетов выводим ошибку
        if quantity == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantity not valid")
        # Считаем общую сумму заказа для конкретного букета
        total_price_for_one_bouquet = price * quantity
        # Добавляем в итоговую сумму всего заказа стоимость одного вида букета
        total_price += total_price_for_one_bouquet
        # Добавляем информацию о букете в лист с букетами
        bouquets.append({"bouquet": bouquet, "quantity": quantity})
    # Если пользователь реферальный, то делаем скидку за приглашение друга
    if user.Ref == 1:
        total_price = int((1 - config.__getattr__("DISCOUNT_INVITE") / 100) * total_price)
        user.Ref = 0
    # Если пользователь не реферальный и хочет списать бонусы, уменьшаем стоимость заказа на количество бонусов
    elif user.Ref != 1 and off_bonus is True:
        count_bonus = user.CountBonus
        # Если количество бонусов меньше, чем нижняя планка стоимости заказа, просто вычитаем бонусы
        if count_bonus < total_price * config.__getattr__("DISCOUNT_BONUS_LIMIT_FOR_PURCHASE") / 100:
            total_price = total_price - count_bonus
            user.CountBonus -= count_bonus
        else:
            # Если же бонусов больше, чем стоимость заказа, уменьшаем стоиомость до нижней планки
            half = int(total_price / config.__getattr__("DISCOUNT_BONUS_LIMIT_FOR_PURCHASE") / 100)
            total_price = total_price - half
            user.CountBonus -= half
    # Если пользователь не реферальный и не хочет списывать бонусы, начисляем бонусы за заказ
    elif user.Ref != 1 and off_bonus is False:
        count_bonus = int(total_price * config.__getattr__("PERCENTAGE_BONUS_FOR_ORDER") / 100)
        user.CountBonus += count_bonus
    # Обновляем пользователя
    await user_services.update_user(user_id, user)
    # Создаем и передаем данные о заказе
    order = await create_order(Order(user_id=user_id, total_price=total_price))
    # Проходим по каждому виду букетов
    for bite in bouquets:
        # Создаем и записываем информацию о купленных букетах в базу данных
        await create_orderbouquets(OrderBouquets(order_id=order.ID,
                                                 bouquet_id=bite["bouquet"].ID,
                                                 quantity=bite["quantity"]))
