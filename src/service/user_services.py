from src.repository import user_repository
from src.database.models import User
from fastapi import HTTPException, status


def get_all_users():
    users = user_repository.get_all_users()
    return [User(**user) for user in users]


def get_user_by_id(user_id: int):
    user = user_repository.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return User(**user) if user else None


def get_user_by_telegram_id(telegram_id: int):
    user = user_repository.get_user_by_telegram_id(telegram_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return User(**user) if user else None


def get_user_by_phone(user_phone: str):
    user = user_repository.get_user_by_phone(user_phone)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return User(**user) if user else None


def create_user(user: User):
    existing_user = get_user_by_telegram_id(user.TelegramID)
    existing_user = get_user_by_phone(user.Phone)
    if existing_user.Phone == user.Phone:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="User already exist")
    user_id = user_repository.create_user(user)
    return get_user_by_id(user_id)


def update_user(user_id: int, user: User):
    existing_users = get_all_users()
    for existing_user in existing_users:
        if existing_user.TelegramID == user.TelegramID and existing_user.ID != user_id:
            raise HTTPException(status_code=status.HTTP_302_FOUND, detail="TelegramID already use")
        if existing_user.Phone == user.Phone and existing_user.ID == user_id:
            raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Phone already use")
    user_repository.update_user(user_id, user)
    return {"message": "User updated successfully"}


def delete_user(user_id: int):
    existing_user = get_user_by_id(user_id)
    user_repository.delete_user(user_id)
    return {"message": "User deleted successfully"}
