from pydantic import BaseModel, Field, StrictStr, StrictInt
from enum import Enum
from typing import Optional, List
from datetime import datetime


class Image(BaseModel):
    """Модель изображений"""
    ID: Optional[int] = Field(None, alias="id")
    Url: Optional[StrictStr] = Field(..., alias="url")


class CompanyData(BaseModel):
    """Модель данных компании"""
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name")
    Disc: StrictStr = Field(..., alias="description")


class User(BaseModel):
    """Модель пользователя"""
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name")
    Phone: StrictStr = Field(..., alias="phone")
    CountBonus: Optional[StrictInt] = Field(0, alias="count_bonus")
    Ref: Optional[StrictInt] = Field(0, alias="referal")


class Order(BaseModel):
    """Модель заказа"""
    ID: Optional[int] = Field(None, alias="id")
    UserID: StrictInt = Field(..., alias="user_id")
    BouquetID: StrictInt = Field(..., alias="bouquet_id")
    Date: Optional[datetime] = Field(None, alias="date")
    Price: StrictInt = Field(..., alias="price")
    Completed: Optional[StrictInt] = Field(None, alias="completed")


class Bouquet(BaseModel):
    """Модель букета"""
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name")
    ImageID: StrictInt = Field(..., alias="image_id")


class Adress(BaseModel):
    """Модель адреса"""
    ID: Optional[int] = Field(None, alias="id")
    Adress: StrictStr = Field(..., alias="adress")
    UserID: StrictInt = Field(..., alias="user_id")

