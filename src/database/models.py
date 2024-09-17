from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, StrictInt


class Image(BaseModel):
    """
    Model of image
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    Url: Optional[StrictStr] = Field(...,
                                     alias="url",
                                     examples=["./src/public/bouquet\76f9f862-8202-493a-a753-fcde4..."])


class CompanyData(BaseModel):
    """
    Model of company
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    Name: StrictStr = Field(...,
                            alias="name",
                            examples=["Зеленый Рэйв"],
                            description="Название компании")
    Disc: StrictStr = Field(...,
                            alias="description",
                            examples=["Зеленый Рэйв"
                                      " - это маленькая просторная зеленая комната,"
                                      " в которой кальяны вмонтированы в зеленые стены"],
                            description="Описание компании")


class User(BaseModel):
    """
    Model of user
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    Name: Optional[StrictStr] = Field(None,
                                      alias="name",
                                      examples=["Porin229"],
                                      description="Имя пользователя")
    TelegramID: StrictInt = Field(...,
                                  alias="telegram_id",
                                  examples=[22],
                                  description="Телеграмм ID")
    Phone: Optional[StrictStr] = Field(None,
                                       alias="phone",
                                       examples=["79128405592"],
                                       description="Номер телефона")
    CountBonus: Optional[StrictInt] = Field(0,
                                            alias="count_bonus",
                                            examples=[1000],
                                            description="Количество накопленных бонусов")
    Ref: Optional[StrictInt] = Field(0,
                                     alias="referal",
                                     examples=[0],
                                     description="Приглашал ли пользователь друга по реферальной ссылке?")


class RefCodes(BaseModel):
    """
    Model of refcodes
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    UserID: StrictInt = Field(...,
                              alias="user_id",
                              examples=[2],
                              description="ID пользователя")
    Code: StrictStr = Field(...,
                            alias="code",
                            examples=["$2b$12$sWu02cjJ2Q3RHcMvuv08LOFeoU8lnWU8YXaF3XMOoECYdkrw.7ZxC"],
                            description="Реферальный код, указыввемый при регистрации нового пользователя")


class Order(BaseModel):
    """
    Model of order
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    UserID: StrictInt = Field(...,
                              alias="user_id",
                              examples=[2],
                              description="ID пользователя")
    Date: Optional[datetime] = Field(None,
                                     alias="date",
                                     examples=[f"{datetime.now()}"],
                                     description="Дата и время создания заказа")
    TotalPrice: StrictInt = Field(...,
                                  alias="total_price",
                                  examples=[230],
                                  description="Итоговая стоимость заказа")


class OrderBouquets(BaseModel):
    """
    Model of bouquet into the order
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    OrderID: StrictInt = Field(...,
                               alias="order_id",
                               examples=[2],
                               description="ID заказа")
    BouquetID: StrictInt = Field(...,
                                 alias="bouquet_id",
                                 examples=[2],
                                 description="ID букета")
    Quantity: StrictInt = Field(...,
                                alias="quantity",
                                examples=[3],
                                description="Количество заказанных букетов одного вида")


class OrderHistory(BaseModel):
    """
    Model of order history
    """
    OrderID: StrictInt = Field(...,
                               alias="order_id",
                               examples=[2],
                               description="ID заказа")
    UserID: StrictInt = Field(...,
                              alias="user_id",
                              examples=[2],
                              description="ID пользователя")
    Date: Optional[datetime] = Field(...,
                                     alias="date",
                                     examples=[f"{datetime.now()}"],
                                     description="Дата и время создания заказа")
    TotalPrice: StrictInt = Field(...,
                                  alias="total_price",
                                  examples=[230],
                                  description="Итоговая стоимость заказа")
    Bouquets: list[OrderBouquets] = Field(..., alias="bouquets",
                                          examples=[
                                              {
                                                  "order_id": 1,
                                                  "bouquet_id": 8,
                                                  "quantity": 2
                                              }
                                          ],
                                          description="Модель обьекта букет")


class BouquetsID(BaseModel):
    """
    Model of list bouquet with ID and quantity
    """
    BouquetID: StrictInt = Field(..., alias="bouquet_id", examples=[2], description="ID букета")
    Quantity: StrictInt = Field(...,
                                alias="quantity",
                                examples=[3],
                                description="Количество букетов одного вида")


class Bouquet(BaseModel):
    """
    Model of bouquet
    """
    ID: Optional[int] = Field(None, alias="id")
    Name: StrictStr = Field(...,
                            alias="name",
                            examples=["Букет красных роз"],
                            description="Название букета")
    Price: StrictInt = Field(...,
                             alias="price",
                             examples=[230],
                             description="Цена букета")
    ImageID: Optional[StrictInt] = Field(None,
                                         alias="image_id",
                                         examples=[2],
                                         description="ID изображения букета")


class Adress(BaseModel):
    """
    Model of adress
    """
    ID: Optional[int] = Field(None,
                              alias="id")
    Adress: StrictStr = Field(...,
                              alias="adress",
                              examples=["Улица Варашилова 9"],
                              description="Адресс доставки, указанный пользователем")
    UserID: StrictInt = Field(...,
                              alias="user_id",
                              examples=[2],
                              description="ID пользователя")
