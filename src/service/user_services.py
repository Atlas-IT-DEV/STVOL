from src.repository import user_repository
from src.database.models import User
from fastapi import HTTPException


def get_all_users():
    users = user_repository.get_all_users()
    return [User(**user) for user in users]


def get_user_by_id(user_id: int):
    user = user_repository.get_user_by_id(user_id)
    return User(**user) if user else None


def get_user_by_telegram_id(user_telegram_id: int):
    user = user_repository.get_user_by_telegram_id(user_telegram_id)
    return User(**user) if user else None


def get_user_by_phone(user_phone: str):
    user = user_repository.get_user_by_phone(user_phone)
    return User(**user) if user else None


def create_user(user: User):
    existing_user = get_user_by_telegram_id(user.TelegramID)
    if existing_user and existing_user.TelegramID == user.TelegramID:
        raise HTTPException(status_code=404, detail="User already exist")
    existing_user = get_user_by_phone(user.Phone)
    if existing_user and existing_user.Phone == user.Phone:
        raise HTTPException(status_code=404, detail="User already exist")
    user_id = user_repository.create_user(user)
    return get_user_by_id(user_id)


def update_user(user_id: int, user: User):
    existing_user = get_user_by_telegram_id(user.TelegramID)
    if existing_user.TelegramID == user.TelegramID:
        raise HTTPException(status_code=404, detail="TelegramID already use")
    existing_user = get_user_by_phone(user.Phone)
    if existing_user.Phone == user.Phone:
        raise HTTPException(status_code=404, detail="Phone already use")
    user_repository.update_user(user_id, user)
    return {"message": "User updated successfully"}


def delete_user(user_id: int):
    user_repository.delete_user(user_id)
    return {"message": "User deleted successfully"}
