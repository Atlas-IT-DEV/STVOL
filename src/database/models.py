from pydantic import BaseModel, Field, StrictStr, StrictInt
from enum import Enum
from typing import Optional, List, Dict
from datetime import datetime


class Image(BaseModel):
    """
    Модель изображений

    "example": {

        "url": "./src/public/bouquet\76f9f862-8202-493a-a753-fcde4..."
    }
    """
    ID: Optional[int] = Field(None, alias="id")
    Url: Optional[StrictStr] = Field(..., alias="url")


class CompanyData(BaseModel):
    """
    Модель данных компании

    "example": {

        "name": "Зеленый Рэйв",

        "description": "Зеленый Рэйв - это маленькая просторная зеленая комната,"
                " в которой кальяны вмонтированы в зеленые стены"
    }
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name")
    Disc: StrictStr = Field(..., alias="description")


class User(BaseModel):
    """
    Модель пользователя

    "example": {

        "name": "Porin229",

        "telegram_id": 22,

        "phone": "79128405592",

        "count_bonus": 1000,

        "referal": 0
    }
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: Optional[StrictStr] = Field(None, alias="name")
    TelegramID: StrictInt = Field(..., alias="telegram_id")
    Phone: Optional[StrictStr] = Field(None, alias="phone")
    CountBonus: Optional[StrictInt] = Field(0, alias="count_bonus")
    Ref: Optional[StrictInt] = Field(0, alias="referal")
    

class RefCodes(BaseModel):
    """
    Модель реферальных кодов

    "example": {

        "user_id": 2,

        "code": "$2b$12$sWu02cjJ2Q3RHcMvuv08LOFeoU8lnWU8YXaF3XMOoECYdkrw.7ZxC"
    }
    """
    UserID: StrictInt = Field(..., alias="user_id")
    Code: StrictStr = Field(..., alias="code")


class Order(BaseModel):
    """
    Модель заказа

    "example": {

        "user_id": 2,

        "date": datetime.now(),

        "total_price": 2340
    }
    """
    ID: Optional[int] = Field(None, alias="id")
    UserID: StrictInt = Field(..., alias="user_id")
    Date: Optional[datetime] = Field(None, alias="date")
    TotalPrice: StrictInt = Field(..., alias="total_price")


class OrderBouquets(BaseModel):
    """
    Модель букетов в каждом отдельном заказе

    "example": {

        "order_id": 2,

        "bouquet_id": 9,

        "quantity": 3
    }
    """
    OrderID: StrictInt = Field(..., alias="order_id")
    BouquetID: StrictInt = Field(..., alias="bouquet_id")
    Quantity: StrictInt = Field(..., alias="quantity")



class OrderHistory(BaseModel):
    """
    Модель истории заказов

    "example": {

        "order_id": 2,

        "user_id": 9,

        "date": datetime.now(),

        "total_price": 2340,

        "bouquets": [

                  {
                    "order_id": 1,

                    "bouquet_id": 8,

                    "quantity": 2
                  }
                ]
    }
    """
    OrderID: StrictInt = Field(..., alias="order_id")
    UserID: StrictInt = Field(..., alias="user_id")
    Date: Optional[datetime] = Field(..., alias="date")
    TotalPrice: StrictInt = Field(..., alias="total_price")
    Bouquets: list[OrderBouquets] = Field(..., alias="bouquets")


class BouquetsID(BaseModel):
    """
    Модель словаря с айди букетами и их количеством

    "example": {

        "bouquet_id": 9,

        "quantity": 3
    }
    """
    BouquetID: StrictInt = Field(..., alias="bouquet_id")
    Quantity: StrictInt = Field(..., alias="quantity")


class Bouquet(BaseModel):
    """
    Модель букета

    "example": {

        "name": "Букет красных роз",

        "price": 9000,

        "image_id": 3
    }
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name")
    Price: StrictInt = Field(..., alias="price")
    ImageID: StrictInt = Field(..., alias="image_id")


class Adress(BaseModel):
    """
    Модель адреса

    "example": {

        "adress": "Улица Варашилова 9",

        "user_id": 9
    }
    """
    ID: Optional[int] = Field(None, alias="id")
    Adress: StrictStr = Field(..., alias="adress")
    UserID: StrictInt = Field(..., alias="user_id")

