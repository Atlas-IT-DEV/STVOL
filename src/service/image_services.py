from src.repository import image_repository
from src.database.models import Image
from fastapi import HTTPException, status

def get_all_images():
    images = image_repository.get_all_images()
    return [Image(**image) for image in images]


def get_image_by_id(image_id: int):
    image = image_repository.get_image_by_id(image_id)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Image not found")
    return Image(**image) if image else None


def create_image(image: Image):
    image_id = image_repository.create_image(image)
    return get_image_by_id(image_id)


def update_image(image_id: int, image: Image):
    existing_image = get_image_by_id(image_id)
    image_repository.update_image(image_id, image)
    return {"message": "Image updated successfully"}


def delete_image(image_id: int):
    existing_image = get_image_by_id(image_id)
    image_repository.delete_image(image_id)
    return {"message": "Image deleted successfully"}
