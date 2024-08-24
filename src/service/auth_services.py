from src.service import user_services, refcode_services
from src.database.models import User, RefCodes
from src.utils.refcode import hashinf
from fastapi import HTTPException, status
from src.utils.custom_logging import setup_logging
log = setup_logging()


def signup(user: User, refcode: str = None):
    # Проверяем ввдено ли имя
    if not user.Name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User name not valid")
    # Проверяем существует ли пользователь с таким же телеграмм айди
    existing_user_telegram_id = user_services.get_user_by_telegram_id(user.TelegramID)
    # Если передается номер телефона, проверяется нет ли такого же
    if user.Phone:
        existing_user_phone = user_services.get_user_by_phone(user.Phone)
    # Создаем нового пользователя
    new_user = user_services.create_user(user)
    # Генерируем реферальный код для пользователя на основе его телеграмм айди
    refcodes = RefCodes(user_id=new_user.ID, code=hashinf(new_user.TelegramID))
    # Сохраняем реферальный код в базе данных
    refcode_services.create_refcode(refcodes)
    # Если передан реферальный код при регистрации, то меняем статус пользователя, обладающего этим реферальным кодом
    # на TRUE
    if refcode:
        ref_user = refcode_services.get_user_by_refcode(refcode)
        ref_user.Ref = 1
        # Обновляем пользователя, которому принадлежит реферальный код
        user_services.update_user(ref_user.ID, ref_user)
    return user


def signin(telegram_id: int):
    existing_user_telegram_id = user_services.get_user_by_telegram_id(telegram_id)
    return existing_user_telegram_id
