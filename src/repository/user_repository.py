from src.database.my_connector import Database
from src.database.models import User
db = Database()


def get_all_users():
    query = "SELECT * FROM Users"
    return db.fetch_all(query)


def get_user_by_id(user_id: int):
    query = "SELECT * FROM Users WHERE id=%s"
    return db.fetch_one(query, (user_id,))


def get_user_by_telegram_id(telegram_id: int):
    query = "SELECT * FROM Users WHERE telegram_id=%s"
    return db.fetch_one(query, (telegram_id,))


def get_user_by_phone(user_phone: str):
    query = "SELECT * FROM Users WHERE phone=%s"
    return db.fetch_one(query, (user_phone,))


def create_user(user: User):
    query = "INSERT INTO users (name, telegram_id, phone, count_bonus, referal) VALUES (%s, %s, %s, %s, %s)"
    params = (user.Name, user.TelegramID, user.Phone, user.CountBonus, user.Ref)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_user(user_id: int, user: User):
    query = "UPDATE users SET name=%s, telegram_id=%s, phone=%s, count_bonus=%s, referal=%s WHERE id=%s"
    params = (user.Name, user.TelegramID, user.Phone, user.CountBonus, user.Ref, user_id)
    db.execute_query(query, params)


def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id=%s"
    db.execute_query(query, (user_id,))
