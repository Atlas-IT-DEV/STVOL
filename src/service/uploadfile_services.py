import os
import uuid
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException, status
from src.service import bouquet_services, image_services
from src.database.models import Bouquet, Image
from aiofiles import open as aio_open
from src.utils.custom_logging import setup_logging
from config import Config
config = Config()
log = setup_logging()


async def uploadfile_bouquet(file, bouquet_name: str, bouquet_price: int):
    # Проверяем введено ли имя букета
    if not bouquet_name:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Name bouquet not define")
    # Проверяем введена ли стомость букета
    if not bouquet_price:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f"Price bouquet not define")
    # Проверяем существует ли букет с таким же именем
    bouquet = await bouquet_services.get_bouquet_by_name(bouquet_name)
    if bouquet:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail="Bouquet already exist")
    else:
        # Получаем расширение файла
        file_extension = file.filename.split('.')[-1]
        # Создаем уникальное имя файла
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        # Записываем путь к файлу
        file_location = os.path.join(config.__getattr__("UPLOAD_DIR"), "bouquet", unique_filename)
        # Проверяем существует ли папка, в которой храняться файлы
        os.makedirs(os.path.join(config.__getattr__("UPLOAD_DIR"), "bouquet"), exist_ok=True)
        # Открывааем файл и записываем данные изображения
        async with aio_open(file_location, "wb") as buffer:
            await buffer.write(await file.read())
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
    return {
        "image_url": f"http://{config.__getattr__('HOST')}:{config.__getattr__('SERVER_PORT')}/"
                     f"public/bouquet/{image.Url.split('/')[-1]}"
    }
