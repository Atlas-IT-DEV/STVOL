import os
import uuid
from fastapi.responses import FileResponse
from fastapi import HTTPException
from src.service import bouquet_services, image_services
from src.database.models import Bouquet, Image
from dotenv import load_dotenv
load_dotenv()
UPLOAD_DIR_BOUQUET = os.getenv('UPLOAD_DIR_BOUQUET')



def uploadfile_bouquet(file, bouquet_name: str, bouquet_price: int):
    # Проверяем введено ли имя букета
    if not bouquet_name:
        raise HTTPException(status_code=404, detail=f"Name bouquet not define")
    # Проверяем введена ли стомость букета
    if not bouquet_price:
        raise HTTPException(status_code=404, detail=f"Price bouquet not define")
    # Проверяем существует ли букет с таким же именем
    bouquet = bouquet_services.get_bouquet_by_name(bouquet_name)
    if bouquet:
        raise HTTPException(status_code=404, detail="Bouquet already exist")
    else:
        # Получаем расширение файла
        file_extension = file.filename.split('.')[-1]
        # Создаем уникальное имя файла
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        # Записываем путь к файлу
        file_location = os.path.join(UPLOAD_DIR_BOUQUET, unique_filename)
        # Проверяем существует ли папка, в которой храняться файлы
        os.makedirs(UPLOAD_DIR_BOUQUET, exist_ok=True)
        # Открывааем файл и записываем данные изображения
        with open(file_location, "wb") as buffer:
            buffer.write(file.read())
        # Создаем информацию в базе данных о пути изображения
        image = image_services.create_image(Image(url=file_location))
        # Создаем и возвращаем букет
        return bouquet_services.create_bouquet(Bouquet(name=bouquet_name,
                                                             price=bouquet_price,
                                                             image_id=image.ID))


def download_bouquet(bouquet_id: int):
    # Проверяем существование букета
    bouquet = bouquet_services.get_bouquet_by_id(bouquet_id)
    if not bouquet:
        raise HTTPException(status_code=404, detail="Bouquet not exist")
    # Проверяем данные в таблице со ссылками на изображения для букета
    image = image_services.get_image_by_id(bouquet.ImageID)
    if not image:
        raise HTTPException(status_code=404, detail="Image not exist")
    # Проверяем существование файла в папке
    if not os.path.exists(image.Url):
        raise HTTPException(status_code=404, detail="File not exist")
    # Возвращаем изображение
    return FileResponse(image.Url)
