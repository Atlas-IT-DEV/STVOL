from src.database.my_connector import Database
from src.database.models import RefCodes
from src.database.my_connector import db


def get_all_refcodes():
    query = "SELECT * FROM ref_codes"
    return db.fetch_all(query)


def get_refcode_by_id(refcode_id: int):
    query = "SELECT * FROM ref_codes WHERE id=%s"
    return db.fetch_one(query, (refcode_id,))


def get_refcode_by_user_id(user_id: int):
    query = "SELECT * FROM ref_codes WHERE user_id=%s"
    return db.fetch_one(query, (user_id,))


def get_user_id_by_refcode(refcode: str):
    query = "SELECT * FROM ref_codes WHERE code=%s"
    return db.fetch_one(query, (refcode,))


def create_refcode(refcodes: RefCodes):
    query = "INSERT INTO ref_codes (user_id, code) VALUES (%s, %s)"
    params = (refcodes.UserID, refcodes.Code)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_refcode(refcode_id: int, refcodes: RefCodes):
    query = "UPDATE ref_codes SET user_id=%s, code=%s WHERE id=%s"
    params = (refcodes.UserID, refcodes.Code, refcode_id)
    db.execute_query(query, params)


def delete_refcode(refcode_id: int):
    query = "DELETE FROM ref_codes WHERE id=%s"
    db.execute_query(query, (refcode_id,))
