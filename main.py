import os
from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.params import Query
from fastapi.staticfiles import StaticFiles
from src.database.my_connector import Database
from typing import Dict
from fastapi.openapi.models import Tag
from fastapi.middleware.cors import CORSMiddleware
from src.service import (user_services, adress_services, order_services, bouquet_services,
                         company_services, refcode_services, image_services, uploadfile_services, auth_services)
from src.database.models import (User, Adress, Order, Bouquet,
                                 CompanyData, RefCodes, Image, BouquetsID, OrderHistory)
from src.utils.custom_logging import setup_logging
from config import Config

config = Config()
log = setup_logging()
app = FastAPI()

app.mount("/bouquet", StaticFiles(directory=os.path.join(config.__getattr__("UPLOAD_DIR"))), name="bouquet")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Определяем теги
AuthTag = Tag(name="Auth", description="Registration and authorization")
UploadFileTag = Tag(name="UploadFile", description="Create object with image saving"
                                                   " and get image by user ID")
UserTag = Tag(name="User", description="CRUD operations user")
AdressTag = Tag(name="Adress", description="CRUD operations adress")
OrderTag = Tag(name="Order", description="CRUD operations, create purchase, get history order")
BouquetTag = Tag(name="Bouquet", description="CRUD operations bouquet")
CompanyTag = Tag(name="Company", description="CRUD operations company")
RefCodeTag = Tag(name="RefCode", description="CRUD operations referal code")
ImageTag = Tag(name="Image", description="CRUD operations image")

# Настройка документации с тегами
app.openapi_tags = [
    AuthTag.dict(),
    UploadFileTag.dict(),
    UserTag.dict(),
    AdressTag.dict(),
    OrderTag.dict(),
    BouquetTag.dict(),
    CompanyTag.dict(),
    RefCodeTag.dict(),
    ImageTag.dict()
]


@app.get("/users/", response_model=list[User], tags=["User"])
async def get_all_users():
    """
    Route for get all users from basedata.

    :return: response model List[User].
    """
    try:
        return user_services.get_all_users()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/users/user_id/{user_id}", response_model=User, tags=["User"])
async def get_user_by_id(user_id: int):
    """
    Route for get user by UserID.

    :param user_id: ID by user. [int]

    :return: response model User.
    """
    try:
        return user_services.get_user_by_id(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/users/telegram_id/{telegram_id}", response_model=User, tags=["User"])
async def get_user_by_telegram_id(telegram_id: int):
    """
    Route for get user by TelegramID.

    :param telegram_id: TelegramID by user. [int]

    :return: response model Order.
    """
    try:
        return user_services.get_user_by_telegram_id(telegram_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/users/", response_model=User, tags=["User"])
async def create_user(user: User):
    """
    Route for create user in basedata.

    :param user: Model user. [User]

    :return: response model User.
    """
    try:
        return user_services.create_user(user)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/users/{user_id}", response_model=Dict, tags=["User"])
async def update_user(user_id: int, user: User):
    """
    Route for update user in basedata.

    :param user_id: ID by user. [int]

    :param user: Model user. [User]

    :return: response model dict.
    """
    try:
        return user_services.update_user(user_id, user)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/users/{user_id}", response_model=Dict, tags=["User"])
async def delete_user(user_id: int):
    """
    Route for delete user from basedata.

    :param user_id: ID by user. [int]

    :return: response model dict.
    """
    try:
        return user_services.delete_user(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/adresses/", response_model=list[Adress], tags=["Adress"])
async def get_all_adresses():
    """
    Route for get all adresses from basedata.

    :return: response model List[Adress].
    """
    try:
        return adress_services.get_all_adresses()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/adresses/adress_id/{adress_id}", response_model=Adress, tags=["Adress"])
async def get_adress_by_id(adress_id: int):
    """
    Route for get adress by AdressID.

    :param adress_id: ID by adress. [int]

    :return: response model Adress.
    """
    try:
        return adress_services.get_adress_by_id(adress_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/adresses/user_id/{user_id}", response_model=list[Adress], tags=["Adress"])
async def get_adress_by_user_id(user_id: int):
    """
    Route for get adress by UserID.

    :param user_id: ID by user. [int]

    :return: response model List[Adress].
    """
    try:
        return adress_services.get_adress_by_user_id(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/adresses/", response_model=Adress, tags=["Adress"])
async def create_adress(adress: Adress):
    """
    Route for create adress in basedata.

    :param adress: Model adress. [Adress]

    :return: response model Adress.
    """
    try:
        return adress_services.create_adress(adress)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/adresses/{adress_id}", response_model=Dict, tags=["Adress"])
async def update_adress(adress_id: int, adress: Adress):
    """
    Route for update adress in basedata.

    :param adress_id: ID by adress. [int]

    :param adress: Model adress. [Adress]

    :return: response model dict.
    """
    try:
        return adress_services.update_adress(adress_id, adress)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/adresses/{adress_id}", response_model=Dict, tags=["Adress"])
async def delete_adress(adress_id: int):
    """
    Route for delete adress from basedata.

    :param adress_id: ID by adress. [int]

    :return: response model dict.
    """
    try:
        return adress_services.delete_adress(adress_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/orders/", response_model=list[Order], tags=["Order"])
async def get_all_orders():
    """
    Route for get all order from basedata.

    :return: response model List[Order].
    """
    try:
        return order_services.get_all_orders()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/orders/order_id/{order_id}", response_model=Order, tags=["Order"])
async def get_order_by_id(order_id: int):
    """
    Route for get order by OrderID.

    :param order_id: ID by order. [int]

    :return: response model Order.
    """
    try:
        return order_services.get_order_by_id(order_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/orders/user_id/{user_id}", response_model=list[Order], tags=["Order"])
async def get_order_by_user_id(user_id: int):
    """
    Route for get order by UserID.

    :param user_id: ID by User. [int]

    :return: response model list[Order].
    """
    try:
        return order_services.get_order_by_user_id(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/orders/", response_model=Order, tags=["Order"])
async def create_order(order: Order):
    """
    Route for create order in basedata.

    :param order: Model order. [Order]

    :return: response model Order.
    """
    try:
        return order_services.create_order(order)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/orders/{order_id}", response_model=Dict, tags=["Order"])
async def update_order(order: Order, order_id: int):
    """
    Route for update order in basedata.

    :param order_id: ID by order. [int]

    :param order: Model order. [Order]

    :return: response model dict.
    """
    try:
        return order_services.update_order(order_id, order)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/orders/{order_id}", response_model=Dict, tags=["Order"])
async def delete_order(order_id: int):
    """
    Route for delete order from basedata.

    :param order_id: ID by order. [int]

    :return: response model dict.
    """
    try:
        return order_services.delete_order(order_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/orders/purchase", response_model=Order, tags=["Order"])
async def buy_create_order(bouquetsID: list[BouquetsID], user_id: int = Form(...), off_bonus: bool = False):
    """
    Route for creating an order using the user ID,
     transmitted information about bouquets with a bonus accounting mechanism.

    :param user_id: ID by User. [int]

    :param bouquetsID: A list containing information about bouquets. [List[BouquetsID]]

    :param off_bonus: A Boolean variable indicating whether to remove the user's bonuses or keep them? [bool]

    :return: response model None.
    """
    try:
        return order_services.buy_create_order(user_id, bouquetsID, off_bonus)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/orders/history/{user_id}", response_model=list[OrderHistory], tags=["Order"])
async def buy_history_order(user_id: int):
    """
    Route for get history by user from basedata.

    :param user_id: ID by User. [int]

    :return: response model List[OrderHistory].
    """
    try:
        return order_services.buy_history_order(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/bouquets/", response_model=list[Bouquet], tags=["Bouquet"])
async def get_all_bouquets():
    """
    Route for get all bouquets from basedata.

    :return: response model List[Bouquet].
    """
    try:
        return bouquet_services.get_all_bouquets()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/bouquets/bouquet_id/{bouquet_id}", response_model=Bouquet, tags=["Bouquet"])
async def get_bouquet_by_id(bouquet_id: int):
    """
    Route for get bouquet by BouquetID.

    :param bouquet_id: ID by bouquet. [int]

    :return: response model Bouquet.
    """
    try:
        return bouquet_services.get_bouquet_by_id(bouquet_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/bouquets/bouquet_name/{bouquet_name}", response_model=Bouquet, tags=["Bouquet"])
async def get_bouquet_by_name(bouquet_name: str):
    """
    Route for get bouquet by name.

    :param bouquet_name: Name by bouquet. [int]

    :return: response model Bouquet.
    """
    try:
        return bouquet_services.get_bouquet_by_name(bouquet_name)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/bouquets/", response_model=Bouquet, tags=["Bouquet"])
async def create_bouquet(bouquet: Bouquet):
    """
    Route for create bouquet in basedata.

    :param bouquet: Model bouquet. [Bouquet]

    :return: response model Bouquet.
    """
    try:
        return bouquet_services.create_bouquet(bouquet)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/bouquets/{bouquet_id}", response_model=Dict, tags=["Bouquet"])
async def update_bouquet(bouquet: Bouquet, bouquet_id: int):
    """
    Route for update bouquet in basedata.

    :param bouquet_id: ID by bouquet. [int]

    :param bouquet: Model bouquet. [Bouquet]

    :return: response model dict.
    """
    try:
        return bouquet_services.update_bouquet(bouquet_id, bouquet)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/bouquets/{bouquet_id}", response_model=Dict, tags=["Bouquet"])
async def delete_bouquet(bouquet_id: int):
    """
    Route for delete bouquet from basedata.

    :param bouquet_id: ID by bouquet. [int]

    :return: response model dict.
    """
    try:
        return bouquet_services.delete_bouquet(bouquet_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/download/get_bouquet/{bouquet_id}", response_model=Dict, tags=["UploadFile"])
async def download_bouquet(bouquet_id: int):
    """
    Route for download image from server on fronted by bouquetID.

    :param bouquet_id: ID by bouquet. [int]

    :return: response model None.
    """
    try:
        return uploadfile_services.download_bouquet(bouquet_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/companys/", response_model=list[CompanyData], tags=["Company"])
async def get_all_companys():
    """
    Route for get all companys from basedata.

    :return: response model List[CompanyData].
    """
    try:
        return company_services.get_all_companys()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/companys/company_id/{company_id}", response_model=CompanyData, tags=["Company"])
async def get_company_by_id(company_id: int):
    """
    Route for get company by CompanyID.

    :param company_id: ID by company. [int]

    :return: response model CompanyData.
    """
    try:
        return company_services.get_company_by_id(company_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/companys/", response_model=CompanyData, tags=["Company"])
async def create_company(company: CompanyData):
    """
    Route for create company in basedata.

    :param company: Model company. [CompanyData]

    :return: response model CompanyData.
    """
    try:
        return company_services.create_company(company)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/companys/{company_id}", response_model=Dict, tags=["Company"])
async def update_company(company: CompanyData, company_id: int):
    """
    Route for update company in basedata.

    :param company_id: ID by company. [int]

    :param company: Model company. [CompanyData]

    :return: response model dict.
    """
    try:
        return company_services.update_company(company_id, company)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/companys/{company_id}", response_model=Dict, tags=["Company"])
async def delete_company(company_id: int):
    """
    Route for delete company from basedata.

    :param company_id: ID by Company. [int]

    :return: response model dict.
    """
    try:
        return company_services.delete_company(company_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/refcodes/", response_model=list[RefCodes], tags=["RefCode"])
async def get_all_refcodes():
    """
    Route for get all referal codes from basedata.

    :return: response model List[Image].
    """
    try:
        return refcode_services.get_all_refcodes()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/refcodes/user_id/{user_id}", response_model=RefCodes, tags=["RefCode"])
async def get_refcode_by_user_id(user_id: int):
    """
    Route for get referal code by UserID.

    :param user_id: ID by User. [int]

    :return: response model RefCodes.
    """
    try:
        return refcode_services.get_refcode_by_user_id(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/refcodes/refcode/{refcode}", response_model=User, tags=["RefCode"])
async def get_user_by_refcode(refcode: str):
    """
    Route for get User by referal code.

    :param refcode: Referal code for invite friend. [str]

    :return: response model User.
    """
    try:
        return refcode_services.get_user_by_refcode(refcode)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/refcodes/", response_model=RefCodes, tags=["RefCode"])
async def create_refcode(refcodes: RefCodes):
    """
    Route for create referal code in basedata.

    :param refcodes: Model refcodes. [RefCodes]

    :return: response model RefCodes.
    """
    try:
        return refcode_services.create_refcode(refcodes)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/refcodes/{user_id}", response_model=Dict, tags=["RefCode"])
async def update_refcode(refcodes: RefCodes, user_id: int):
    """
    Route for update referal code in basedata.

    :param user_id: ID by User. [int]

    :param refcodes: Model RefCodes. [RefCodes]

    :return: response model dict.
    """
    try:
        return refcode_services.update_refcode(user_id, refcodes)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/refcodes/{user_id}", response_model=Dict, tags=["RefCode"])
async def delete_refcode(user_id: int):
    """
    Route for delete referal code from basedata.

    :param user_id: ID by User. [int]

    :return: response model dict.
    """
    try:
        return refcode_services.delete_refcode(user_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/images/", response_model=list[Image], tags=["Image"])
async def get_all_images():
    """
    Route for get all image from basedata.

    :return: response model List[Image].
    """
    try:
        return image_services.get_all_images()
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.get("/images/image_id/{image_id}", response_model=Image, tags=["Image"])
async def get_image_by_id(image_id: int):
    """
    Route for get image by imageID.

    :param image_id: ID by image. [int]

    :return: response model Image.
    """
    try:
        return image_services.get_image_by_id(image_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/images/", response_model=Image, tags=["Image"])
async def create_image(image: Image):
    """
    Route for create image in basedata.

    :param image: Model image. [Image]

    :return: response model Image.
    """
    try:
        return image_services.create_image(image)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.put("/images/{image_id}", response_model=Dict, tags=["Image"])
async def update_image(image: Image, image_id: int):
    """
    Route for update image in basedata.

    :param image_id: ID by image. [int]

    :param image: Model image. [Image]

    :return: response model dict.
    """
    try:
        return image_services.update_image(image_id, image)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.delete("/images/{image_id}", response_model=Dict, tags=["Image"])
async def delete_image(image_id: int):
    """
    Route for delete image from basedata.

    :param image_id: ID by image. [int]

    :return: response model dict.
    """
    try:
        image_services.delete_image(image_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/signup/", response_model=User, tags=["Auth"])
async def signup(user: User, refcode: str = Query(None)):
    """
    Route for user registration.

    :param user: Model User. [User]

    :param refcode: Referal code for invite friend. [str]

    :return: response model User.
    """
    try:
        return auth_services.signup(user, refcode)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/signin/", response_model=User, tags=["Auth"])
async def signin(telegram_id: str):
    """
    Route for user authorization.

    :param telegram_id: telegramID of user. [int]

    :return: response model User.
    """
    try:
        return auth_services.signin(telegram_id)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


@app.post("/uploadfile/create_bouquet/", response_model=Bouquet, tags=["UploadFile"])
async def uploadfile_bouquet(file: UploadFile = File(...),
                             bouquet_name: str = Form(...), bouquet_price: int = Form(...)):
    """
    Route for uploading an image of a bouquet and transferring it to the server,
     followed by creating a bouquet in the database with a link to the image of the bouquet.

    :param file: Binary image file. [str]

    :param bouquet_name: Name by bouquet. [str]

    :param bouquet_price: Price by bouquet in ruble. [int]

    :return: response model Bouquet.
    """
    try:
        return await uploadfile_services.uploadfile_bouquet(file, bouquet_name, bouquet_price)
    except HTTPException as ex:
        log.exception(f"Error", exc_info=ex)
        raise ex


def run_server():
    import logging
    import uvicorn
    import yaml
    uvicorn_log_config = 'logging.yaml'
    with open(uvicorn_log_config, 'r') as f:
        uvicorn_config = yaml.safe_load(f.read())
        logging.config.dictConfig(uvicorn_config)
    uvicorn.run("main:app", host=config.__getattr__("HOST"), port=int(config.__getattr__("SERVER_PORT")),
                reload=True, log_config=uvicorn_log_config)


def run_bot():
    from src.telegram_bot.main import StvolBot
    bot = StvolBot()
    bot.start_bot()


if __name__ == "__main__":

    # Создание датабазы и таблиц, если они не существуют
    log.info("Start create/update database")
    from create_sql import CreateSQL
    create_sql = CreateSQL()
    create_sql.read_sql()

    # Запуск сервера и бота
    log.info("Start run server and bot")
    import multiprocessing
    server_process = multiprocessing.Process(target=run_server)
    server_process.start()
    bot_process = multiprocessing.Process(target=run_bot)
    bot_process.start()
    server_process.join()
    bot_process.join()
