from src.database.my_connector import Database
from src.database.models import Bouquet
db = Database()


async def get_all_bouquets():
    query = "SELECT * FROM Bouquet"
    return await db.fetch_all(query)


async def get_bouquet_by_id(bouquet_id: int):
    query = "SELECT * FROM Bouquet WHERE id=%s"
    return await db.fetch_one(query, (bouquet_id,))


async def create_bouquet(bouquet: Bouquet):
    query = "INSERT INTO Bouquet (name, image_id) VALUES (%s, %s)"
    params = (bouquet.Name, bouquet.ImageID)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_bouquet(bouquet_id: int, bouquet: Bouquet):
    query = "UPDATE Bouquet SET name=%s, image_id=%s WHERE id=%s"
    params = (bouquet.Name, bouquet.ImageID, bouquet_id)
    await db.execute_query(query, params)


async def delete_bouquet(bouquet_id: int):
    query = "DELETE FROM Bouquet WHERE id=%s"
    await db.execute_query(query, (bouquet_id,))
