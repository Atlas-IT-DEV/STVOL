import os
from fastapi import HTTPException, status
from src.repository import bouquet_repository, bouquet_repository
from src.service import image_services
from src.database.models import Bouquet
from src.utils.custom_logging import setup_logging
from src.utils.exam_services import check_if_exists, check_for_duplicates
from src.service.image_services import get_image_by_id
from src.utils.return_url_object import return_url_object
log = setup_logging()


def get_all_bouquets(dirs: bool = False):
    bouquets = bouquet_repository.get_all_bouquets()
    models = [Bouquet(**bouquet) for bouquet in bouquets]
    list_bouquets = []
    for bouquet in bouquets:
        try:
            # Получаем список изображений по ID букета
            url = get_image_by_id(bouquet["image_id"])
            url = return_url_object(url.Url)
        except Exception as e:
            url = None
        bouquet["url"] = url
        del bouquet["image_id"]
        list_bouquets.append(bouquet)
    if dirs:
        return list_bouquets
    else:
        return models


def get_bouquet_by_id(bouquet_id: int, dirs: bool = False):
    bouquet = bouquet_repository.get_bouquet_by_id(bouquet_id)
    if not bouquet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bouquet not found")
    model = Bouquet(**bouquet) if bouquet else None
    try:
        # Получаем список изображений по ID букета
        url = get_image_by_id(bouquet["image_id"])
        url = return_url_object(url.Url)
    except Exception as e:
        url = None
    bouquet["url"] = url
    del bouquet["image_id"]
    if dirs:
        return bouquet
    else:
        return model


def get_bouquet_by_name(bouquet_name: str):
    bouquet = bouquet_repository.get_bouquet_by_name(bouquet_name)
    if not bouquet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bouquet not found")
    return Bouquet(**bouquet) if bouquet else None


def create_bouquet(bouquet: Bouquet):
    check_if_exists(
        get_all=get_all_bouquets,
        attr_name="Name",
        attr_value=bouquet.Name,
        exception_detail='Name already exist'
    )
    bouquet_id = bouquet_repository.create_bouquet(bouquet)
    return get_bouquet_by_id(bouquet_id)


def update_bouquet(bouquet_id: int, bouquet: Bouquet):
    check_for_duplicates(
        get_all=get_all_bouquets,
        check_id=bouquet_id,
        attr_name="Name",
        attr_value=bouquet.Name,
        exception_detail='Name already exist'
    )
    bouquet_repository.update_bouquet(bouquet_id, bouquet)
    return {"message": "Bouquet updated successfully"}


def delete_bouquet(bouquet_id: int):
    bouquet = get_bouquet_by_id(bouquet_id)
    image = image_services.get_image_by_id(bouquet.ImageID)
    # Удаление изображение букета
    if os.path.exists(image.Url):
        os.remove(image.Url)
    else:
        log.warning(f"Warning: File {image.Url} not found")
    # Удаляем сам букет
    bouquet_repository.delete_bouquet(bouquet_id)
    # Удаляем записи о букете в таблице с путями изображений
    image_services.delete_image(image.ID)
    return {"message": "Bouquet deleted successfully"}
