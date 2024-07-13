from src.repository import refcode_repository, user_repository
from src.database.models import RefCodes, User


async def get_all_refcodes():
    refcodes = await refcode_repository.get_all_refcodes()
    return [RefCodes(**refcode) for refcode in refcodes]


async def get_refcode_by_user_id(user_id: int):
    refcode = await refcode_repository.get_refcode_by_user_id(user_id)
    return RefCodes(**refcode) if refcode else None


async def get_user_by_refcode(refcode: str):
    refcodes = await refcode_repository.get_user_id_by_refcode(refcode)
    user = await user_repository.get_user_by_id(refcodes["user_id"])
    return User(**user) if user else None


async def create_refcode(refcodes: RefCodes):
    user_id = await refcode_repository.create_refcode(refcodes)
    return await get_refcode_by_user_id(user_id)


async def update_refcode(user_id: int, refcodes: RefCodes):
    await refcode_repository.update_refcode(user_id, refcodes)
    return {"message": "RefCode updated successfully"}


async def delete_refcode(user_id: int):
    await refcode_repository.delete_refcode(user_id)
    return {"message": "RefCode deleted successfully"}
