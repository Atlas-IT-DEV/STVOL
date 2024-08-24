import os
from src.repository import order_repository
from src.service import user_services, bouquet_services
from src.database.models import Order, OrderBouquets, OrderHistory
from fastapi import HTTPException, status
from config import Config
from src.utils.custom_logging import setup_logging
config = Config()
log = setup_logging()


def get_all_orders():
    orders = order_repository.get_all_orders()
    return [Order(**order) for order in orders]


def get_order_by_id(order_id: int):
    order = order_repository.get_order_by_id(order_id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Order not found')
    return Order(**order) if order else None


def get_orderbouquets_by_order_id(order_id: int):
    existing_order = get_order_by_id(order_id)
    orderbouquets = order_repository.get_orderbouquets_by_order_id(order_id)
    return [OrderBouquets(**orderbouquet) for orderbouquet in orderbouquets]


def get_order_by_user_id(user_id: int):
    existing_user = user_services.get_user_by_id(user_id)
    orders = order_repository.get_order_by_user_id(user_id)
    return [Order(**order) for order in orders]


def create_order(order: Order):
    order_id = order_repository.create_order(order)
    return get_order_by_id(order_id)


def create_orderbouquets(orderbouquets: OrderBouquets):
    order_id = order_repository.create_orderbouquets(orderbouquets)
    return get_order_by_id(order_id)


def update_order(order_id: int, order: Order):
    existing_order = get_order_by_id(order_id)
    order_repository.update_order(order_id, order)
    return {"message": "Order updated successfully"}


def delete_order(order_id: int):
    existing_order = get_order_by_id(order_id)
    order_repository.delete_order(order_id)
    return {"message": "Order deleted successfully"}


def buy_history_order(user_id: int):
    # Проверяем существоние пользователя
    user = user_services.get_user_by_id(user_id)
    # Получаем заказы пользователя
    orders = get_order_by_user_id(user_id)
    history = []
    # Проходим по всем заказам
    for order in orders:
        # Получаем информацию о букетах и их количестве для заказа
        orderbouquets = get_orderbouquets_by_order_id(order.ID)
        # Создаем и записываем в модель историю заказа
        orderhistory = OrderHistory(order_id=order.ID,
                                    user_id=order.UserID,
                                    date=order.Date,
                                    total_price=order.TotalPrice,
                                    bouquets=orderbouquets)
        # Добавляем историю заказа в список
        history.append(orderhistory)
    return history


def buy_create_order(user_id, bouquetsID, off_bonus):
    # Проверяем существоание пользователя
    user = user_services.get_user_by_id(user_id)
    bouquets = []
    total_price = 0
    # Проходим по каждому букету в переданном листе.
    for bouquetID in bouquetsID:
        # Проверяем существование букета
        bouquet = bouquet_services.get_bouquet_by_id(bouquetID.BouquetID)
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
    user_services.update_user(user_id, user)
    # Создаем и передаем данные о заказе
    order = create_order(Order(user_id=user_id, total_price=total_price))
    # Проходим по каждому виду букетов
    for bite in bouquets:
        # Создаем и записываем информацию о купленных букетах в базу данных
        create_orderbouquets(OrderBouquets(order_id=order.ID,
                                           bouquet_id=bite["bouquet"].ID,
                                           quantity=bite["quantity"]))
    return order
