from src.database.my_connector import Database
from src.database.models import Order, OrderBouquets
db = Database()


async def get_all_orders():
    query = "SELECT * FROM Orders"
    return await db.fetch_all(query)


async def get_order_by_id(order_id: int):
    query = "SELECT * FROM Orders WHERE id=%s"
    return await db.fetch_one(query, (order_id,))


async def get_order_by_user_id(user_id: int):
    query = "SELECT * FROM Orders WHERE user_id=%s"
    return await db.fetch_all(query, (user_id,))


async def get_orderbouquets_by_order_id(order_id: int):
    query = "SELECT * FROM Order_Bouquets Where order_id=%s"
    return await db.fetch_all(query, (order_id,))


async def create_order(order: Order):
    query = "INSERT INTO Orders (user_id, total_price) VALUES (%s, %s)"
    params = (order.UserID, order.TotalPrice)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def create_orderbouquets(orderbouquets: OrderBouquets):
    query = "INSERT INTO Order_Bouquets (order_id, bouquet_id, quantity) VALUES (%s, %s, %s)"
    params = (orderbouquets.OrderID, orderbouquets.BouquetID, orderbouquets.Quantity)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_order(order_id: int, order: Order):
    query = "UPDATE Orders SET user_id=%s, total_price=%s WHERE id=%s"
    params = (order.UserID, order.TotalPrice, order_id)
    await db.execute_query(query, params)


async def delete_order(order_id: int):
    query = "DELETE FROM Orders WHERE id=%s"
    await db.execute_query(query, (order_id,))
