import os
from fastapi import HTTPException, status
from src.repository import bouquet_repository, bouquet_repository
from src.service import image_services
from src.database.models import Bouquet
from src.utils.custom_logging import setup_logging
log = setup_logging()


async def get_all_bouquets():
    bouquets = bouquet_repository.get_all_bouquets()
    return [Bouquet(**bouquet) for bouquet in bouquets]


async def get_bouquet_by_id(bouquet_id: int):
    bouquet = bouquet_repository.get_bouquet_by_id(bouquet_id)
    return Bouquet(**bouquet) if bouquet else None


async def get_bouquet_by_name(bouquet_name: str):
    bouquet = bouquet_repository.get_bouquet_by_name(bouquet_name)
    return Bouquet(**bouquet) if bouquet else None


async def create_bouquet(bouquet: Bouquet):
    bouquet_id = bouquet_repository.create_bouquet(bouquet)
    return await get_bouquet_by_id(bouquet_id)


async def update_bouquet(bouquet_id: int, bouquet: Bouquet):
    bouquet_repository.update_bouquet(bouquet_id, bouquet)
    return {"message": "Bouquet updated successfully"}


async def delete_bouquet(bouquet_id: int):
    # Проверка существования букета
    bouquet = await get_bouquet_by_id(bouquet_id)
    if not bouquet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bouquet not exist")
    # Проверка существования информации о пути изображения букета
    image = await image_services.get_image_by_id(bouquet.ImageID)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not exist")
    # Удаление изображение букета
    if os.path.exists(image.Url):
        os.remove(image.Url)
    else:
        log.warning(f"Warning: File {image.Url} not found")
    # Удаляем сам букет
    bouquet_repository.delete_bouquet(bouquet_id)
    # Удаляем записи о букете в таблице с путями изображений
    await image_services.delete_image(image.ID)
    return {"message": "Bouquet deleted successfully"}
