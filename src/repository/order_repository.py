from src.database.my_connector import Database
from src.database.models import Order
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


async def create_order(order: Order):
    query = "INSERT INTO Orders (user_id, bouquet_id, price) VALUES (%s, %s, %s)"
    params = (order.UserID, order.BouquetID, order.Price)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_order(order_id: int, order: Order):
    query = "UPDATE Orders SET user_id=%s, bouquet_id=%s, price=%s, completed=%s WHERE id=%s"
    params = (order.UserID, order.BouquetID, order.Price, order.Completed, order_id)
    await db.execute_query(query, params)


async def delete_order(order_id: int):
    query = "DELETE FROM Orders WHERE id=%s"
    await db.execute_query(query, (order_id,))
