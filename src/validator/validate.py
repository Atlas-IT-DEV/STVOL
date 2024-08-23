from pydantic import BaseModel, ValidationError
from typing import Type, Any
from src.database.models import Twitt


def check_valid(model: Type[BaseModel], data: Any) -> bool:
    """
    Function for validation response model. \n
    :param model: Sample model. [Type[BaseModel]] \n
    :param data: Response model. [Type[BaseModel]] \n
    :return: bool.
    """
    try:
        model(**data)
        return True
    except ValidationError as e:
        print(f"Validation error: {e}")
        return False

