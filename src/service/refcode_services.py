from src.repository import refcode_repository
from src.service import user_services
from src.database.models import RefCodes, User
from fastapi import HTTPException, status


def get_all_refcodes():
    refcodes = refcode_repository.get_all_refcodes()
    return [RefCodes(**refcode) for refcode in refcodes]


def get_refcode_by_id(refcode_id: int):
    refcode = refcode_repository.get_refcode_by_id(refcode_id)
    if not refcode:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Refcode not found')
    return RefCodes(**refcode) if refcode else None


def get_refcode_by_user_id(user_id: int):
    refcode = refcode_repository.get_refcode_by_user_id(user_id)
    if not refcode:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Refcode not found')
    return RefCodes(**refcode) if refcode else None


def get_user_by_refcode(refcode: str):
    refcodes = refcode_repository.get_user_id_by_refcode(refcode)
    user = user_services.get_user_by_id(refcodes["user_id"])
    return User(**user) if user else None


def create_refcode(refcodes: RefCodes):
    refcode_id = refcode_repository.create_refcode(refcodes)
    return get_refcode_by_id(refcode_id)


def update_refcode(refcode_id: int, refcodes: RefCodes):
    refcode_id = refcode_repository.get_refcode_by_id(refcode_id)
    refcode_repository.update_refcode(refcode_id, refcodes)
    return {"message": "RefCode updated successfully"}


def delete_refcode(refcode_id: int):
    get_refcode_by_id(refcode_id)
    refcode_repository.delete_refcode(refcode_id)
    return {"message": "RefCode deleted successfully"}
