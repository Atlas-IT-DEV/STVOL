from src.database.my_connector import Database
from src.database.models import Bouquet
from src.database.my_connector import db


def get_all_bouquets():
    query = "SELECT * FROM Bouquet"
    return db.fetch_all(query)


def get_bouquet_by_id(bouquet_id: int):
    query = "SELECT * FROM Bouquet WHERE id=%s"
    return db.fetch_one(query, (bouquet_id,))


def get_bouquet_by_name(bouquet_name: str):
    query = "SELECT * FROM Bouquet WHERE name=%s"
    return db.fetch_one(query, (bouquet_name,))


def create_bouquet(bouquet: Bouquet):
    query = "INSERT INTO Bouquet (name, price, image_id) VALUES (%s, %s, %s)"
    params = (bouquet.Name, bouquet.Price, bouquet.ImageID)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_bouquet(bouquet_id: int, bouquet: Bouquet):
    query = "UPDATE Bouquet SET name=%s, price=%s, image_id=%s WHERE id=%s"
    params = (bouquet.Name, bouquet.Price, bouquet.ImageID, bouquet_id)
    db.execute_query(query, params)


def delete_bouquet(bouquet_id: int):
    query = "DELETE FROM Bouquet WHERE id=%s"
    db.execute_query(query, (bouquet_id,))

