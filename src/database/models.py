from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, StrictInt


class Image(BaseModel):
    """
    Model of image
    """
    ID: Optional[int] = Field(None, alias="id")
    Url: Optional[StrictStr] = Field(..., alias=["url"],
                                     examples=["./src/public/bouquet\76f9f862-8202-493a-a753-fcde4..."])


class CompanyData(BaseModel):
    """
    Model of company
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name", examples=["Зеленый Рэйв"])
    Disc: StrictStr = Field(..., alias="description", examples=["Зеленый Рэйв"
                                                                " - это маленькая просторная зеленая комната,"
                                                                " в которой кальяны вмонтированы в зеленые стены"])


class User(BaseModel):
    """
    Model of user
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: Optional[StrictStr] = Field(None, alias="name", examples=["Porin229"])
    TelegramID: StrictInt = Field(..., alias="telegram_id", examples=[22])
    Phone: Optional[StrictStr] = Field(None, alias="phone", examples=["79128405592"])
    CountBonus: Optional[StrictInt] = Field(0, alias="count_bonus", examples=[1000])
    Ref: Optional[StrictInt] = Field(0, alias="referal", examples=[0])


class RefCodes(BaseModel):
    """
    Model of refcodes
    """
    UserID: StrictInt = Field(..., alias="user_id", examples=[2])
    Code: StrictStr = Field(..., alias="code", examples=["$2b$12$sWu02cjJ2Q3RHcMvuv08LO"
                                                         "FeoU8lnWU8YXaF3XMOoECYdkrw.7ZxC"])


class Order(BaseModel):
    """
    Model of order
    """
    ID: Optional[int] = Field(None, alias="id")
    UserID: StrictInt = Field(..., alias="user_id", examples=[2])
    Date: Optional[datetime] = Field(None, alias="date", examples=[datetime.now()])
    TotalPrice: StrictInt = Field(..., alias="total_price", examples=[230])


class OrderBouquets(BaseModel):
    """
    Model of bouquet into the order
    """
    OrderID: StrictInt = Field(..., alias="order_id", examples=[2])
    BouquetID: StrictInt = Field(..., alias="bouquet_id", examples=[2])
    Quantity: StrictInt = Field(..., alias="quantity", examples=[3])


class OrderHistory(BaseModel):
    """
    Model of order history
    """
    OrderID: StrictInt = Field(..., alias="order_id", examples=[2])
    UserID: StrictInt = Field(..., alias="user_id", examples=[2])
    Date: Optional[datetime] = Field(..., alias="date", examples=[datetime.now()])
    TotalPrice: StrictInt = Field(..., alias="total_price", examples=[230])
    Bouquets: list[OrderBouquets] = Field(..., alias="bouquets",
                                          examples=[
                                              {
                                                  "order_id": 1,
                                                  "bouquet_id": 8,
                                                  "quantity": 2
                                              }
                                          ])


class BouquetsID(BaseModel):
    """
    Model of list bouquet with ID and quantity
    """
    BouquetID: StrictInt = Field(..., alias="bouquet_id", examples=[2])
    Quantity: StrictInt = Field(..., alias="quantity", examples=[3])


class Bouquet(BaseModel):
    """
    Model of bouquet
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(..., alias="name", examples=["Букет красных роз"])
    Price: StrictInt = Field(..., alias="price", examples=[230])
    ImageID: StrictInt = Field(..., alias="image_id", examples=[2])


class Adress(BaseModel):
    """
    Model of adress
    """
    ID: Optional[int] = Field(None, alias="id")
    Adress: StrictStr = Field(..., alias="adress", examples=["Улица Варашилова 9"])
    UserID: StrictInt = Field(..., alias="user_id", examples=[2])
