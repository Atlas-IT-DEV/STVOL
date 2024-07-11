from src.repository import bouquet_repository
from src.database.models import Bouquet


async def get_all_bouquets():
    bouquets = await bouquet_repository.get_all_bouquets()
    return [Bouquet(**bouquet) for bouquet in bouquets]


async def get_bouquet_by_id(bouquet_id: int):
    bouquet = await bouquet_repository.get_bouquet_by_id(bouquet_id)
    return Bouquet(**bouquet) if bouquet else None


async def create_bouquet(bouquet: Bouquet):
    bouquet_id = await bouquet_repository.create_bouquet(bouquet)
    return await get_bouquet_by_id(bouquet_id)


async def update_bouquet(bouquet_id: int, bouquet: Bouquet):
    await bouquet_repository.update_bouquet(bouquet_id, bouquet)
    return {"message": "Bouquet updated successfully"}


async def delete_bouquet(bouquet_id: int):
    await bouquet_repository.delete_bouquet(bouquet_id)
    return {"message": "Bouquet deleted successfully"}
