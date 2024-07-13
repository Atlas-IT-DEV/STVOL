from src.repository import order_repository
from src.database.models import Order, OrderBouquets


async def get_all_orders():
    orders = await order_repository.get_all_orders()
    return [Order(**order) for order in orders]


async def get_order_by_id(order_id: int):
    order = await order_repository.get_order_by_id(order_id)
    return Order(**order) if order else None


async def get_orderbouquets_by_order_id(order_id: int):
    orderbouquets = await order_repository.get_orderbouquets_by_order_id(order_id)
    return [OrderBouquets(**orderbouquet) for orderbouquet in orderbouquets]


async def get_order_by_user_id(user_id: int):
    orders = await order_repository.get_order_by_user_id(user_id)
    return [Order(**order) for order in orders]


async def create_order(order: Order):
    order_id = await order_repository.create_order(order)
    return await get_order_by_id(order_id)


async def create_orderbouquets(orderbouquets: OrderBouquets):
    order_id = await order_repository.create_orderbouquets(orderbouquets)
    return await get_order_by_id(order_id)


async def update_order(order_id: int, order: Order):
    await order_repository.update_order(order_id, order)
    return {"message": "Order updated successfully"}


async def delete_order(order_id: int):
    await order_repository.delete_order(order_id)
    return {"message": "Order deleted successfully"}
