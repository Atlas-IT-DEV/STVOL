from src.database.my_connector import Database
from src.database.models import Adress
db = Database()


async def get_all_adresses():
    query = "SELECT * FROM Adresses"
    return await db.fetch_all(query)


async def get_adress_by_id(adress_id: int):
    query = "SELECT * FROM Adresses WHERE id=%s"
    return await db.fetch_one(query, (adress_id,))


async def get_adress_by_user_id(user_id: int):
    query = "SELECT * FROM Adresses WHERE user_id=%s"
    return await db.fetch_all(query, (user_id,))


async def create_adress(adress: Adress):
    query = "INSERT INTO Adresses (adress, user_id) VALUES (%s, %s)"
    params = (adress.Adress, adress.UserID)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_adress(adress_id: int, adress: Adress):
    query = "UPDATE Adresses SET adress=%s, user_id=%s WHERE id=%s"
    params = (adress.Adress, adress.UserID, adress_id)
    await db.execute_query(query, params)


async def delete_adress(adress_id: int):
    query = "DELETE FROM Adresses WHERE id=%s"
    await db.execute_query(query, (adress_id,))
