import os
import uuid
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException, status, Depends
from src.service import bouquet_services, image_services
from src.database.models import Bouquet, Image
from src.utils.return_url_object import return_url_object
from src.utils.write_file_into_server import write_file_into_server
from aiofiles import open as aio_open
from src.utils.custom_logging import setup_logging
from config import Config
config = Config()
log = setup_logging()


async def uploadfile_bouquet(file, bouquet_name: str, bouquet_price: int):
    if not bouquet_name:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bouquet name not define")
    if not bouquet_price:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Price not defined")
    # Проверяем существует ли букет с таким же именем
    bouquet = await bouquet_services.get_bouquet_by_name(bouquet_name)
    if bouquet:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Bouquet already exist")
    else:
        # Записываем файл на сервер
        unique_filename = await write_file_into_server("bouquet", file)
        # Создаем информацию в базе данных о пути изображения
        image = await image_services.create_image(Image(url=f"/bouquet/{unique_filename}"))
        # Создаем и возвращаем букет
        return await bouquet_services.create_bouquet(Bouquet(name=bouquet_name,
                                                       price=bouquet_price,
                                                       image_id=image.ID))


async def download_bouquet(bouquet_id: int):
    # Проверяем существование букета
    bouquet = await bouquet_services.get_bouquet_by_id(bouquet_id)
    if not bouquet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bouquet not exist")
    # Проверяем данные в таблице со ссылками на изображения для букета
    image = await image_services.get_image_by_id(bouquet.ImageID)
    if not image:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Image not exist")
    # Проверяем существование файла в папке
    log.debug(config.__getattr__("UPLOAD_DIR") + "bouquet" + image.Url.split("/")[-1])
    if not os.path.exists(os.path.join(config.__getattr__("UPLOAD_DIR"),"bouquet",image.Url.split("/")[-1])):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not exists")
    # return FileResponse(image.Url)
    return return_url_object(image, "bouquet", bouquet.dict())
