from src.database.my_connector import Database
from src.database.models import Order, OrderBouquets
from src.database.my_connector import db


def get_all_orders():
    query = "SELECT * FROM Orders"
    return db.fetch_all(query)


def get_order_by_id(order_id: int):
    query = "SELECT * FROM Orders WHERE id=%s"
    return db.fetch_one(query, (order_id,))


def get_order_by_user_id(user_id: int):
    query = "SELECT * FROM orders WHERE user_id=%s"
    return db.fetch_all(query, (user_id,))


def get_orderbouquets_by_order_id(order_id: int):
    query = "SELECT * FROM order_bouquets Where order_id=%s"
    return db.fetch_all(query, (order_id,))


def create_order(order: Order):
    query = "INSERT INTO orders (user_id, date, total_price) VALUES (%s, %s, %s)"
    params = (order.UserID, order.Date, order.TotalPrice)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def create_orderbouquets(orderbouquets: OrderBouquets):
    query = "INSERT INTO order_bouquets (order_id, bouquet_id, quantity) VALUES (%s, %s, %s)"
    params = (orderbouquets.OrderID, orderbouquets.BouquetID, orderbouquets.Quantity)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_order(order_id: int, order: Order):
    query = "UPDATE orders SET user_id=%s, date=%s, total_price=%s WHERE id=%s"
    params = (order.UserID, order.Date, order.TotalPrice, order_id)
    db.execute_query(query, params)


def delete_order(order_id: int):
    query = "DELETE FROM orders WHERE id=%s"
    db.execute_query(query, (order_id,))
