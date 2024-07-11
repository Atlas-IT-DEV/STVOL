from src.database.my_connector import Database
from src.database.models import User
db = Database()


async def get_all_users():
    query = "SELECT * FROM Users"
    return await db.fetch_all(query)


async def get_user_by_id(user_id: int):
    query = "SELECT * FROM Users WHERE id=%s"
    return await db.fetch_one(query, (user_id,))


async def get_user_by_phone(user_phone: str):
    query = "SELECT * FROM Users WHERE phone=%s"
    return await db.fetch_one(query, (user_phone,))


async def create_user(user: User):
    query = "INSERT INTO users (name, phone, count_bonus, referal) VALUES (%s, %s, %s, %s)"
    params = (user.Name, user.Phone, user.CountBonus, user.Ref)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_user(user_id: int, user: User):
    query = "UPDATE users SET name=%s, phone=%s, count_bonus=%s, referal=%s WHERE id=%s"
    params = (user.Name, user.Phone, user.CountBonus, user.Ref, user_id)
    await db.execute_query(query, params)


async def delete_user(user_id: int):
    query = "DELETE FROM users WHERE id=%s"
    await db.execute_query(query, (user_id,))
