from src.repository import image_repository
from src.database.models import Image


async def get_all_images():
    images = image_repository.get_all_images()
    return [Image(**image) for image in images]


async def get_image_by_id(image_id: int):
    image = image_repository.get_image_by_id(image_id)
    return Image(**image) if image else None


async def create_image(image: Image):
    image_id = image_repository.create_image(image)
    return await get_image_by_id(image_id)


async def update_image(image_id: int, image: Image):
    image_repository.update_image(image_id, image)
    return {"message": "Image updated successfully"}


async def delete_image(image_id: int):
    image_repository.delete_image(image_id)
    return {"message": "Image deleted successfully"}
