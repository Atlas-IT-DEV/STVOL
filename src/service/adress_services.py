from src.repository import adress_repository
from src.database.models import Adress
from src.service.user_services import get_user_by_id
from fastapi import HTTPException, status


def get_all_adresses():
    adresses = adress_repository.get_all_adresses()
    return [Adress(**adress) for adress in adresses]


def get_adress_by_id(adress_id: int):
    adress = adress_repository.get_adress_by_id(adress_id)
    if not adress:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Adress not found')
    return Adress(**adress) if adress else None


def get_adress_by_user_id(user_id: int):
    adresses = adress_repository.get_adress_by_user_id(user_id)
    if not adresses:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Adresses not found')
    return [Adress(**adress) for adress in adresses]


def create_adress(adress: Adress):
    existing_user = get_user_by_id(adress.UserID)
    adress_id = adress_repository.create_adress(adress)
    return get_adress_by_id(adress_id)


def update_adress(adress_id: int, adress: Adress):
    existing_adress = get_adress_by_id(adress_id)
    existing_user = get_user_by_id(adress.UserID)
    adress_repository.update_adress(adress_id, adress)
    return {"message": "Adress updated successfully"}


def delete_adress(adress_id: int):
    existing_adress = get_adress_by_id(adress_id)
    adress_repository.delete_adress(adress_id)
    return {"message": "Adress deleted successfully"}
