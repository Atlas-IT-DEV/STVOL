from src.database.my_connector import Database
from src.database.models import RefCodes
db = Database()


async def get_all_refcodes():
    query = "SELECT * FROM Ref_Codes"
    return await db.fetch_all(query)


async def get_refcode_by_user_id(user_id: int):
    query = "SELECT * FROM Ref_Codes WHERE user_id=%s"
    return await db.fetch_one(query, (user_id,))


async def get_user_id_by_refcode(refcode: str):
    query = "SELECT * FROM Ref_Codes WHERE code=%s"
    return await db.fetch_one(query, (refcode,))


async def create_refcode(refcodes: RefCodes):
    query = "INSERT INTO Ref_Codes (user_id, code) VALUES (%s, %s)"
    params = (refcodes.UserID, refcodes.Code)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_refcode(user_id: int, refcodes: RefCodes):
    query = "UPDATE Ref_Codes SET code=%s WHERE user_id=%s"
    params = (refcodes.Code, user_id)
    await db.execute_query(query, params)


async def delete_refcode(user_id: int):
    query = "DELETE FROM Ref_Codes WHERE user_id=%s"
    await db.execute_query(query, (user_id,))
