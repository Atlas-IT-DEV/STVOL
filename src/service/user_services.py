from src.repository import user_repository
from src.database.models import User
from fastapi import HTTPException, status


async def get_all_users():
    users = user_repository.get_all_users()
    return [User(**user) for user in users]


async def get_user_by_id(user_id: int):
    user = user_repository.get_user_by_id(user_id)
    return User(**user) if user else None


async def get_user_by_telegram_id(user_telegram_id: int):
    user = user_repository.get_user_by_telegram_id(user_telegram_id)
    return User(**user) if user else None


async def get_user_by_phone(user_phone: str):
    user = user_repository.get_user_by_phone(user_phone)
    return User(**user) if user else None


async def create_user(user: User):
    existing_user = await get_user_by_telegram_id(user.TelegramID)
    if existing_user and existing_user.TelegramID == user.TelegramID:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="User already exist")
    existing_user = await get_user_by_phone(user.Phone)
    if existing_user and existing_user.Phone == user.Phone:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="User already exist")
    user_id = user_repository.create_user(user)
    return await get_user_by_id(user_id)


async def update_user(user_id: int, user: User):
    existing_user = await get_user_by_telegram_id(user.TelegramID)
    if existing_user.TelegramID == user.TelegramID:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="TelegramID already use")
    existing_user = await get_user_by_phone(user.Phone)
    if existing_user.Phone == user.Phone:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Phone already use")
    user_repository.update_user(user_id, user)
    return {"message": "User updated successfully"}


async def delete_user(user_id: int):
    user_repository.delete_user(user_id)
    return {"message": "User deleted successfully"}
