from src.service import user_services, refcode_services
from src.database.models import User, RefCodes
from src.utils.refcode import hashinf
from fastapi import HTTPException


async def signon(user: User, refcode: str):
    # Проверяем ввдено ли имя
    if not user.Name:
        raise HTTPException(status_code=404, detail="User name not valid")
    # Проверяем существует ли пользователь с таким же телеграмм айди
    existing_user_telegram_id = await user_services.get_user_by_telegram_id(user.TelegramID)
    if existing_user_telegram_id:
        raise HTTPException(status_code=404, detail="User already exist")
    # Если передается номер телефона, проверяется нет ли такого же
    if user.Phone:
        existing_user_phone = await user_services.get_user_by_phone(user.Phone)
        if existing_user_phone:
            raise HTTPException(status_code=404, detail="User already exist")
    # Создаем нового пользователя
    new_user = await user_services.create_user(user)
    # Генерируем реферальный код для пользователя на основе его телеграмм айди
    refcodes = RefCodes(user_id=new_user.ID, code=hashinf(new_user.TelegramID))
    # Сохраняем реферальный код в базе данных
    await refcode_services.create_refcode(refcodes)
    # Если передан реферальный код при регистрации, то меняем статус пользователя, обладающего этим реферальным кодом на TRUE
    if refcode:
        ref_user = await refcode_services.get_user_by_refcode(refcode)
        ref_user.Ref = 1
        # Обновляем пользователя, которому принадлежит реферальный код
        await user_services.update_user(ref_user.ID, ref_user)
    return user


async def signin(user: User):
    existing_user_telegram_id = await user_services.get_user_by_telegram_id(user.TelegramID)
    if not existing_user_telegram_id:
        raise HTTPException(status_code=404, detail="User not exist")
    if user.Phone:
        existing_user_phone = await user_services.get_user_by_phone(user.Phone)
        if not existing_user_phone:
            raise HTTPException(status_code=404, detail="User not exist")
    else:
        return existing_user_telegram_id

