import os
from fastapi import HTTPException, status, UploadFile
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.database.models import Bouquet, Image
from src.utils.write_file_into_server import write_file_into_server
from src.utils.return_url_object import return_url_object
from src.service.image_services import get_image_by_id, update_image, create_image
from src.service.bouquet_services import get_bouquet_by_id, update_bouquet, create_bouquet
from src.utils.custom_logging import setup_logging
from config import Config

config = Config()
log = setup_logging()


async def upload_images(file: UploadFile,
                        bouquet_name: str,
                        bouquet_price: int):
    # Создаем сущность
    existing_bouquet = create_bouquet(Bouquet(name=bouquet_name,
                                              price=bouquet_price))
    # Записываем файл на сервер
    unique_filename = await write_file_into_server('bouquet', file)
    # Формируем ссылку на изображение
    url = return_url_object(f"/bouquet/{unique_filename}")
    # Создаем информацию в таблице image
    image = create_image(Image(url=url))
    # Обновляем созданную сущность
    existing_bouquet.ImageID = image.ID
    update_bouquet(existing_bouquet.ID, existing_bouquet)
    return get_bouquet_by_id(existing_bouquet.ID)


def delete_images(entity_type: str, entity_id: int,
                  get_entity_by_id, update_entity):
    existing_entity = get_entity_by_id(entity_id)
    image = get_image_by_id(existing_entity.ImageID)
    url = image.Url
    if not existing_entity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Entity with ID {entity_id} not found")
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Image {entity_type} with ID {entity_id} not exist")
    file_path = os.path.join(config.__getattr__("UPLOAD_DIR"), entity_type, url.split("/")[-1])
    if os.path.exists(file_path):
        os.remove(file_path)
        log.info(f"File {file_path} deleted successfully.")
    else:
        log.warning(f"File {file_path} does not exist.")
    image.Url = None
    update_image(image.ID, image)
    log.info(f"Image entity record with ID {entity_id} deleted from database.")
    return {
        "status": "success"
    }
