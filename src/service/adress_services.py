from src.repository import adress_repository
from src.database.models import Adress
from src.service.user_services import get_user_by_id
from fastapi import HTTPException, status
from src.utils.exam_services import check_if_exists, check_for_duplicates


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
    check_if_exists(
        get_all=get_all_adresses,
        attr_name="Adress",
        attr_value=adress.Adress,
        exception_detail='Adress already exist'
    )
    adress_id = adress_repository.create_adress(adress)
    return get_adress_by_id(adress_id)


def update_adress(adress_id: int, adress: Adress):
    check_for_duplicates(
        get_all=get_all_adresses,
        check_id=adress_id,
        attr_name="Adress",
        attr_value=adress.Adress,
        exception_detail='Adress already exist'
    )
    adress_repository.update_adress(adress_id, adress)
    return {"message": "Adress updated successfully"}


def delete_adress(adress_id: int):
    get_adress_by_id(adress_id)
    adress_repository.delete_adress(adress_id)
    return {"message": "Adress deleted successfully"}
