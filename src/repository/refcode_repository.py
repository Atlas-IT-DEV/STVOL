from src.database.my_connector import Database
from src.database.models import RefCodes
db = Database()


def get_all_refcodes():
    query = "SELECT * FROM Ref_Codes"
    return db.fetch_all(query)


def get_refcode_by_user_id(user_id: int):
    query = "SELECT * FROM Ref_Codes WHERE user_id=%s"
    return db.fetch_one(query, (user_id,))


def get_user_id_by_refcode(refcode: str):
    query = "SELECT * FROM Ref_Codes WHERE code=%s"
    return db.fetch_one(query, (refcode,))


def create_refcode(refcodes: RefCodes):
    query = "INSERT INTO Ref_Codes (user_id, code) VALUES (%s, %s)"
    params = (refcodes.UserID, refcodes.Code)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_refcode(user_id: int, refcodes: RefCodes):
    query = "UPDATE Ref_Codes SET code=%s WHERE user_id=%s"
    params = (refcodes.Code, user_id)
    db.execute_query(query, params)


def delete_refcode(user_id: int):
    query = "DELETE FROM Ref_Codes WHERE user_id=%s"
    db.execute_query(query, (user_id,))
