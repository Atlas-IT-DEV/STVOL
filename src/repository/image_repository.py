from src.database.my_connector import Database
from src.database.models import Image
db = Database()


def get_all_images():
    query = "SELECT * FROM Images"
    return db.fetch_all(query)


def get_image_by_id(image_id: int):
    query = "SELECT * FROM Images WHERE id=%s"
    return db.fetch_one(query, (image_id,))


def create_image(image: Image):
    query = "INSERT INTO Images (url) VALUES (%s)"
    params = image.Url
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_image(image_id: int, image: Image):
    query = "UPDATE Images SET url=%s WHERE id=%s"
    params = (image.Url, image_id)
    db.execute_query(query, params)


def delete_image(image_id: int):
    query = "DELETE FROM Images WHERE id=%s"
    db.execute_query(query, (image_id,))
