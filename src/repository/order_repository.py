from src.database.my_connector import Database
from src.database.models import Order, OrderBouquets
db = Database()


def get_all_orders():
    query = "SELECT * FROM Orders"
    return db.fetch_all(query)


def get_order_by_id(order_id: int):
    query = "SELECT * FROM Orders WHERE id=%s"
    return db.fetch_one(query, (order_id,))


def get_order_by_user_id(user_id: int):
    query = "SELECT * FROM Orders WHERE user_id=%s"
    return db.fetch_all(query, (user_id,))


def get_orderbouquets_by_order_id(order_id: int):
    query = "SELECT * FROM Order_Bouquets Where order_id=%s"
    return db.fetch_all(query, (order_id,))


def create_order(order: Order):
    query = "INSERT INTO Orders (user_id, total_price) VALUES (%s, %s)"
    params = (order.UserID, order.TotalPrice)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def create_orderbouquets(orderbouquets: OrderBouquets):
    query = "INSERT INTO Order_Bouquets (order_id, bouquet_id, quantity) VALUES (%s, %s, %s)"
    params = (orderbouquets.OrderID, orderbouquets.BouquetID, orderbouquets.Quantity)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_order(order_id: int, order: Order):
    query = "UPDATE Orders SET user_id=%s, total_price=%s WHERE id=%s"
    params = (order.UserID, order.TotalPrice, order_id)
    db.execute_query(query, params)


def delete_order(order_id: int):
    query = "DELETE FROM Orders WHERE id=%s"
    db.execute_query(query, (order_id,))
