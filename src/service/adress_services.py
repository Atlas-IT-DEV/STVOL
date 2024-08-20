from src.repository import adress_repository
from src.database.models import Adress


def get_all_adresses():
    adresses = adress_repository.get_all_adresses()
    return [Adress(**adress) for adress in adresses]


def get_adress_by_id(adress_id: int):
    adress = adress_repository.get_adress_by_id(adress_id)
    return Adress(**adress) if adress else None


def get_adress_by_user_id(user_id: int):
    adresses = adress_repository.get_adress_by_user_id(user_id)
    return [Adress(**adress) for adress in adresses]


def create_adress(adress: Adress):
    adress_id = adress_repository.create_adress(adress)
    return get_adress_by_id(adress_id)


def update_adress(adress_id: int, adress: Adress):
    adress_repository.update_adress(adress_id, adress)
    return {"message": "Adress updated successfully"}


def delete_adress(adress_id: int):
    adress_repository.delete_adress(adress_id)
    return {"message": "Adress deleted successfully"}
