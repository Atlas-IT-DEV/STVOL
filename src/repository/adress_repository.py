from src.database.my_connector import Database
from src.database.models import Adress
from src.database.my_connector import db


def get_all_adresses():
    query = "SELECT * FROM adresses"
    return db.fetch_all(query)


def get_adress_by_id(adress_id: int):
    query = "SELECT * FROM adresses WHERE id=%s"
    return db.fetch_one(query, (adress_id,))


def get_adress_by_user_id(user_id: int):
    query = "SELECT * FROM adresses WHERE user_id=%s"
    return db.fetch_all(query, (user_id,))


def create_adress(adress: Adress):
    query = "INSERT INTO adresses (adress, user_id) VALUES (%s, %s)"
    params = (adress.Adress, adress.UserID)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_adress(adress_id: int, adress: Adress):
    query = "UPDATE adresses SET adress=%s, user_id=%s WHERE id=%s"
    params = (adress.Adress, adress.UserID, adress_id)
    db.execute_query(query, params)


def delete_adress(adress_id: int):
    query = "DELETE FROM adresses WHERE id=%s"
    db.execute_query(query, (adress_id,))
