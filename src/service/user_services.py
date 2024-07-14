from src.repository import user_repository
from src.database.models import User


async def get_all_users():
    users = await user_repository.get_all_users()
    return [User(**user) for user in users]


async def get_user_by_id(user_id: int):
    user = await user_repository.get_user_by_id(user_id)
    return User(**user) if user else None


async def get_user_by_telegram_id(user_telegram_id: int):
    user = await user_repository.get_user_by_telegram_id(user_telegram_id)
    return User(**user) if user else None


async def get_user_by_phone(user_phone: str):
    user = await user_repository.get_user_by_phone(user_phone)
    return User(**user) if user else None


async def create_user(user: User):
    user_id = await user_repository.create_user(user)
    return await get_user_by_id(user_id)


async def update_user(user_id: int, user: User):
    await user_repository.update_user(user_id, user)
    return {"message": "User updated successfully"}


async def delete_user(user_id: int):
    await user_repository.delete_user(user_id)
    return {"message": "User deleted successfully"}
