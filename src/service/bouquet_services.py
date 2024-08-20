import os
from fastapi import HTTPException
from src.repository import bouquet_repository, bouquet_repository
from src.service import image_services
from src.database.models import Bouquet
from src.utils.custom_logging import setup_logging
log = setup_logging()


def get_all_bouquets():
    bouquets = bouquet_repository.get_all_bouquets()
    return [Bouquet(**bouquet) for bouquet in bouquets]


def get_bouquet_by_id(bouquet_id: int):
    bouquet = bouquet_repository.get_bouquet_by_id(bouquet_id)
    return Bouquet(**bouquet) if bouquet else None


def get_bouquet_by_name(bouquet_name: str):
    bouquet = bouquet_repository.get_bouquet_by_name(bouquet_name)
    return Bouquet(**bouquet) if bouquet else None


def create_bouquet(bouquet: Bouquet):
    bouquet_id = bouquet_repository.create_bouquet(bouquet)
    return get_bouquet_by_id(bouquet_id)


def update_bouquet(bouquet_id: int, bouquet: Bouquet):
    bouquet_repository.update_bouquet(bouquet_id, bouquet)
    return {"message": "Bouquet updated successfully"}


def delete_bouquet(bouquet_id: int):
    # Проверка существования букета
    bouquet = get_bouquet_by_id(bouquet_id)
    if not bouquet:
        raise HTTPException(status_code=404, detail="Bouquet not exist")
    # Проверка существования информации о пути изображения букета
    image = image_services.get_image_by_id(bouquet.ImageID)
    if not image:
        raise HTTPException(status_code=404, detail="Image not exist")
    # Удаление изображение букета
    if os.path.exists(image.Url):
        os.remove(image.Url)
    else:
        log.warning(f"Warning: File {image.Url} not found")
    # Удаляем сам букет
    bouquet_repository.delete_bouquet(bouquet_id)
    # Удаляем записи о букете в таблице с путями изображений
    image_services.delete_image(image.ID)
    log.info(f"Bouquet {bouquet_id} deleted successfully")
    return {"message": "Bouquet deleted successfully"}
