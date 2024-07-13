from src.repository import image_repository
from src.database.models import Image


async def get_all_images():
    images = await image_repository.get_all_images()
    return [Image(**image) for image in images]


async def get_image_by_id(image_id: int):
    image = await image_repository.get_image_by_id(image_id)
    return Image(**image) if image else None


async def create_image(image: Image):
    image_id = await image_repository.create_image(image)
    return await get_image_by_id(image_id)


async def update_image(image_id: int, image: Image):
    await image_repository.update_image(image_id, image)
    return {"message": "Image updated successfully"}


async def delete_image(image_id: int):
    await image_repository.delete_image(image_id)
    return {"message": "Image deleted successfully"}
