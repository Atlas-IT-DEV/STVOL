from pydantic import BaseModel, Field, StrictStr, StrictInt
from enum import Enum
from typing import Optional, List, Dict
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


class RefCodes(BaseModel):
    """Модель реферальных кодов"""
    UserID: StrictInt = Field(..., alias="user_id")
    Code: StrictStr = Field(..., alias="code")


class Order(BaseModel):
    """Модель заказа"""
    ID: Optional[int] = Field(None, alias="id")
    UserID: StrictInt = Field(..., alias="user_id")
    Date: Optional[datetime] = Field(None, alias="date")
    TotalPrice: StrictInt = Field(..., alias="total_price")


class OrderBouquets(BaseModel):
    """Модель букетов в каждом отдельном заказе"""
    OrderID: StrictInt = Field(..., alias="order_id")
    BouquetID: StrictInt = Field(..., alias="bouquet_id")
    Quantity: StrictInt = Field(..., alias="quantity")


class OrderHistory(BaseModel):
    """Модель истории заказов"""
    OrderID: StrictInt = Field(..., alias="order_id")
    UserID: StrictInt = Field(..., alias="user_id")
    Date: Optional[datetime] = Field(..., alias="date")
    TotalPrice: StrictInt = Field(..., alias="total_price")
    Bouquets: list[OrderBouquets] = Field(..., alias="bouquets")


class BouquetsID(BaseModel):
    """Модель словаря с айди букетами и их количеством"""
    BouquetID: StrictInt = Field(...)
    Quantity: StrictInt = Field(...)


class Bouquet(BaseModel):
    """Модель букета"""
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name")
    Price: StrictInt = Field(..., alias="price")
    ImageID: StrictInt = Field(..., alias="image_id")


class Adress(BaseModel):
    """Модель адреса"""
    ID: Optional[int] = Field(None, alias="id")
    Adress: StrictStr = Field(..., alias="adress")
    UserID: StrictInt = Field(..., alias="user_id")

