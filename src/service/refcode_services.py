from src.repository import refcode_repository, user_repository
from src.database.models import RefCodes, User


def get_all_refcodes():
    refcodes = refcode_repository.get_all_refcodes()
    return [RefCodes(**refcode) for refcode in refcodes]


def get_refcode_by_user_id(user_id: int):
    refcode = refcode_repository.get_refcode_by_user_id(user_id)
    return RefCodes(**refcode) if refcode else None


def get_user_by_refcode(refcode: str):
    refcodes = refcode_repository.get_user_id_by_refcode(refcode)
    user = user_repository.get_user_by_id(refcodes["user_id"])
    return User(**user) if user else None


def create_refcode(refcodes: RefCodes):
    user_id = refcode_repository.create_refcode(refcodes)
    return get_refcode_by_user_id(user_id)


def update_refcode(user_id: int, refcodes: RefCodes):
    refcode_repository.update_refcode(user_id, refcodes)
    return {"message": "RefCode updated successfully"}


def delete_refcode(user_id: int):
    refcode_repository.delete_refcode(user_id)
    return {"message": "RefCode deleted successfully"}
