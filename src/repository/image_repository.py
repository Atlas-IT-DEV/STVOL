from src.database.my_connector import Database
from src.database.models import Image
db = Database()


async def get_all_images():
    query = "SELECT * FROM Images"
    return await db.fetch_all(query)


async def get_image_by_id(image_id: int):
    query = "SELECT * FROM Images WHERE id=%s"
    return await db.fetch_one(query, (image_id,))


async def create_image(image: Image):
    query = "INSERT INTO Images (url) VALUES (%s)"
    params = image.Url
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_image(image_id: int, image: Image):
    query = "UPDATE Images SET url=%s WHERE id=%s"
    params = (image.Url, image_id)
    await db.execute_query(query, params)


async def delete_image(image_id: int):
    query = "DELETE FROM Images WHERE id=%s"
    await db.execute_query(query, (image_id,))
