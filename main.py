import os
import uuid
import os
from fastapi import FastAPI, HTTPException, File, UploadFile
from src.database.my_connector import Database
from typing import Dict
from fastapi.openapi.models import Tag
from fastapi.middleware.cors import CORSMiddleware
from src.service import (user_services, adress_services, order_services, bouquet_services,
                         company_services, refcode_services, image_services)
from src.database.models import (User, Adress, Order, Bouquet,
                                 CompanyData, RefCodes, Image, BouquetsID, OrderBouquets, OrderHistory)
from src.utils.refcode import hash_phone, check_refcode
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


UPLOAD_DIR_BOUQUET = "./src/public/bouquet"


db = Database()
app = FastAPI()

app.mount("/static", StaticFiles(directory=UPLOAD_DIR_BOUQUET), name="bouquet")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Определяем теги
TestTag = Tag(name="Test", description="Маршрут для тестирования")
AuthTag = Tag(name="Auth", description="Регистрация и авторизация")
BouquetFileTag = Tag(name="BouquetFile", description="Создание букета с сохранением изображения"
                                                     " и получение изображения букета по ID")
BuyTag = Tag(name="Buy", description="Формирование заказа пользователем и расчет бонусов и"
                                     "получение истории заказов пользователя")
UserTag = Tag(name="User", description="CRUD операции пользователь")
AdressTag = Tag(name="Adress", description="CRUD операции адресс")
OrderTag = Tag(name="Order", description="CRUD операции заказ")
BouquetTag = Tag(name="Bouquet", description="CRUD операции букет")
CompanyTag = Tag(name="Company", description="CRUD операции компании")
RefCodeTag = Tag(name="RefCode", description="CRUD операции реферального кода")
ImageTag = Tag(name="Image", description="CRUD операции изображения")

# Настройка документации с тегами
app.openapi_tags = [
    TestTag.dict(),
    AuthTag.dict(),
    BuyTag.dict(),
    BouquetFileTag.dict(),
    UserTag.dict(),
    AdressTag.dict(),
    OrderTag.dict(),
    BouquetTag.dict(),
    CompanyTag.dict(),
    RefCodeTag.dict(),
    ImageTag.dict()
]


@app.on_event("startup")
async def startup_event():
    connected = await db.connect()


@app.get("/", response_model=Dict, tags=["Test"])
async def Test():
    return {"Test": "Normaly Work"}


@app.get("/users/", response_model=list[User], tags=["User"])
async def get_all_users():
    return await user_services.get_all_users()


@app.get("/users/id/{user_id}", response_model=User, tags=["User"])
async def get_user_by_id(user_id: int):
    return await user_services.get_user_by_id(user_id)


@app.get("/users/phone/{user_phone}", response_model=User, tags=["User"])
async def get_user_by_phone(user_phone: str):
    return await user_services.get_user_by_phone(user_phone)


@app.post("/users/", response_model=User, tags=["User"])
async def create_user(user: User):
    return await user_services.create_user(user)


@app.put("/users/{user_id}", response_model=Dict, tags=["User"])
async def update_user(user_id, user: User):
    return await user_services.update_user(user_id, user)


@app.delete("/users/{user_id}", response_model=Dict, tags=["User"])
async def delete_user(user_id):
    return await user_services.delete_user(user_id)


@app.get("/adresses/", response_model=list[Adress], tags=["Adress"])
async def get_all_adresses():
    return await adress_services.get_all_adresses()


@app.get("/adresses/id/{adress_id}", response_model=Adress, tags=["Adress"])
async def get_adress_by_id(adress_id: int):
    return await adress_services.get_adress_by_id(adress_id)


@app.get("/adresses/user/{user_id}", response_model=list[Adress], tags=["Adress"])
async def get_adress_by_user_id(user_id: int):
    return await adress_services.get_adress_by_user_id(user_id)


@app.post("/adresses/", response_model=Adress, tags=["Adress"])
async def create_adress(adress: Adress):
    return await adress_services.create_adress(adress)


@app.put("/adresses/{adress_id}", response_model=Dict, tags=["Adress"])
async def update_adress(adress_id, adress: Adress):
    return await adress_services.update_adress(adress_id, adress)


@app.delete("/adresses/{adress_id}", response_model=Dict, tags=["Adress"])
async def delete_adress(adress_id):
    return await adress_services.delete_adress(adress_id)


@app.get("/orders/", response_model=list[Order], tags=["Order"])
async def get_all_orders():
    return await order_services.get_all_orders()


@app.get("/orders/id/{order_id}", response_model=Order, tags=["Order"])
async def get_order_by_id(order_id: int):
    return await order_services.get_order_by_id(order_id)


@app.get("/orders/user/{user_id}", response_model=list[Order], tags=["Order"])
async def get_order_by_user_id(user_id: int):
    return await order_services.get_order_by_user_id(user_id)


@app.post("/orders/", response_model=Order, tags=["Order"])
async def create_order(order: Order):
    return await order_services.create_order(order)


@app.put("/orders/{order_id}", response_model=Dict, tags=["Order"])
async def update_order(order_id, order: Order):
    return await order_services.update_order(order_id, order)


@app.delete("/orders/{order_id}", response_model=Dict, tags=["Order"])
async def delete_order(order_id):
    return await order_services.delete_order(order_id)


@app.get("/bouquets/", response_model=list[Bouquet], tags=["Bouquet"])
async def get_all_bouquets():
    return await bouquet_services.get_all_bouquets()


@app.get("/bouquets/id/{bouquet_id}", response_model=Bouquet, tags=["Bouquet"])
async def get_bouquet_by_id(bouquet_id: int):
    return await bouquet_services.get_bouquet_by_id(bouquet_id)


@app.get("/bouquets/name/{bouquet_name}", response_model=Bouquet, tags=["Bouquet"])
async def get_bouquet_by_name(bouquet_name: str):
    return await bouquet_services.get_bouquet_by_name(bouquet_name)


@app.post("/bouquets/", response_model=Bouquet, tags=["Bouquet"])
async def create_bouquet(bouquet: Bouquet):
    return await bouquet_services.create_bouquet(bouquet)


@app.put("/bouquets/{bouquet_id}", response_model=Dict, tags=["Bouquet"])
async def update_bouquet(bouquet_id, bouquet: Bouquet):
    return await bouquet_services.update_bouquet(bouquet_id, bouquet)


@app.delete("/bouquets/{bouquet_id}", response_model=Dict, tags=["Bouquet"])
async def delete_bouquet(bouquet_id):
    bouquet = await bouquet_services.get_bouquet_by_id(bouquet_id)
    if not bouquet:
        raise HTTPException(status_code=404, detail="Bouquet not exist")
    image = await image_services.get_image_by_id(bouquet.ImageID)
    if not image:
        raise HTTPException(status_code=404, detail="Image not exist")
    file_path = image.Url
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print(f"Warning: File {file_path} not found")
    await image_services.delete_image(image.ID)
    return await bouquet_services.delete_bouquet(bouquet_id)


@app.get("/companys/", response_model=list[CompanyData], tags=["Company"])
async def get_all_companys():
    return await company_services.get_all_companys()


@app.get("/companys/id/{company_id}", response_model=CompanyData, tags=["Company"])
async def get_company_by_id(company_id: int):
    return await company_services.get_company_by_id(company_id)


@app.post("/companys/", response_model=CompanyData, tags=["Company"])
async def create_company(company: CompanyData):
    return await company_services.create_company(company)


@app.put("/companys/{company_id}", response_model=Dict, tags=["Company"])
async def update_company(company_id, company: CompanyData):
    return await company_services.update_company(company_id, company)


@app.delete("/companys/{company_id}", response_model=Dict, tags=["Company"])
async def delete_company(company_id):
    return await company_services.delete_company(company_id)


@app.get("/refcodes/", response_model=list[RefCodes], tags=["RefCode"])
async def get_all_refcodes():
    return await refcode_services.get_all_refcodes()


@app.get("/refcodes/user/{user_id}", response_model=RefCodes, tags=["RefCode"])
async def get_refcode_by_user_id(user_id: int):
    return await refcode_services.get_refcode_by_user_id(user_id)


@app.get("/refcodes/refcode/{refcode}", response_model=User, tags=["RefCode"])
async def get_user_by_refcode(refcode: str):
    return await refcode_services.get_user_by_refcode(refcode)


@app.post("/refcodes/", response_model=RefCodes, tags=["RefCode"])
async def create_refcode(refcodes: RefCodes):
    return await refcode_services.create_refcode(refcodes)


@app.put("/refcodes/{user_id}", response_model=Dict, tags=["RefCode"])
async def update_refcode(user_id, refcodes: RefCodes):
    return await refcode_services.update_refcode(user_id, refcodes)


@app.delete("/refcodes/{user_id}", response_model=Dict, tags=["RefCode"])
async def delete_refcode(user_id):
    return await refcode_services.delete_refcode(user_id)


@app.get("/images/", response_model=list[Image], tags=["Image"])
async def get_all_images():
    return await image_services.get_all_images()


@app.get("/images/image/{image_id}", response_model=Image, tags=["Image"])
async def get_image_by_id(image_id: int):
    return await image_services.get_image_by_id(image_id)


@app.post("/images/", response_model=Image, tags=["Image"])
async def create_image(image: Image):
    return await image_services.create_image(image)


@app.put("/images/{image_id}", response_model=Dict, tags=["Image"])
async def update_image(image_id, image: Image):
    return await rimage_services.update_image(image_id, image)


@app.delete("/images/{image_id}", response_model=Dict, tags=["Image"])
async def delete_image(image_id):
    return await image_services.delete_image(image_id)


@app.post("/register/", response_model=User, tags=["Auth"])
async def register(user: User, refcode: str = None):
    try:
        existing_user = await user_services.get_user_by_phone(user.Phone)
        if existing_user:
            raise HTTPException(status_code=404, detail="User already exist")
        new_user = await user_services.create_user(user)
        refcodes = RefCodes(user_id=new_user.ID, code=hash_phone(new_user.Phone))
        await refcode_services.create_refcode(refcodes)
        if refcode:
            ref_user = await refcode_services.get_user_by_refcode(refcode)
            ref_user.Ref = 1
            await user_services.update_user(ref_user.ID, ref_user)
        return user
    except Exception as ex:
        print(f"Error {ex}")



@app.post("/login/", response_model=User, tags=["Auth"])
async def login(user: User):
    existing_user = await user_services.get_user_by_phone(user.Phone)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not exist")
    else:
        return existing_user


@app.post("/uploadfile/create_bouquet/{name_bouquet}", response_model=Bouquet, tags=["BouquetFile"])
async def uploadfile_bouquet(file: UploadFile = File(...), bouquet_name: str = None, bouquet_price: int = None):
    try:
        if not bouquet_name:
            raise HTTPException(status_code=404, detail=f"Name bouquet not define")
        if not bouquet_price:
            raise HTTPException(status_code=404, detail=f"Price bouquet not define")
        file_extension = file.filename.split('.')[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        file_location = os.path.join(UPLOAD_DIR_BOUQUET, unique_filename)
        os.makedirs(UPLOAD_DIR_BOUQUET, exist_ok=True)
        with open(file_location, "wb") as buffer:
            buffer.write(await file.read())
        bouquet = await bouquet_services.get_bouquet_by_name(bouquet_name)
        if bouquet:
            raise HTTPException(status_code=404, detail="Bouquet already exist")
        image = await image_services.create_image(Image(url=file_location))
        return await bouquet_services.create_bouquet(Bouquet(name=bouquet_name,
                                                             price=bouquet_price,
                                                             image_id=image.ID))
    except Exception as ex:
        print(f"Error {ex}")
        raise HTTPException(status_code=500, detail=f"File not save. Error: {ex}")


@app.get("/download/get_bouquet/{bouquet_id}", response_model=None, tags=["BouquetFile"])
async def download_bouquet(bouquet_id: int):
    try:
        bouquet = await bouquet_services.get_bouquet_by_id(bouquet_id)
        if not bouquet:
            raise HTTPException(status_code=404, detail="Bouquet not exist")
        image = await image_services.get_image_by_id(bouquet.ImageID)
        if not image:
            raise HTTPException(status_code=404, detail="Image not exist")
        file_path = image.Url
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not exist")
        return FileResponse(file_path)
    except Exception as ex:
        print(f"Error {ex}")
        raise HTTPException(status_code=500, detail=f"File not get. Error: {ex}")


@app.post("/buy/create_order/", response_model=None, tags=["Buy"])
async def buy_create_order(user_id: int, bouquetsID: list[BouquetsID], off_bonus: bool = False):
    try:
        user = await user_services.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not exist")
        bouquets = []
        total_price = 0
        for bouquetID in bouquetsID:
            bouquet = await bouquet_services.get_bouquet_by_id(bouquetID.BouquetID)
            price = bouquet.Price
            quantity = bouquetID.Quantity
            total_price_for_one_bouquet = price * quantity
            total_price += total_price_for_one_bouquet
            if not bouquet:
                raise HTTPException(status_code=404, detail="Bouquet not exist")
            bouquets.append({"bouquet": bouquet, "quantity": quantity})
        if user.Ref == 1:
            total_price = int(0.85 * total_price)
            user.Ref = 0
        elif user.Ref != 1 and off_bonus is True:
            count_bonus = user.CountBonus
            if count_bonus < total_price * 0.5:
                total_price = total_price - count_bonus
                user.CountBonus -= count_bonus
            else:
                half = int(total_price / 2)
                total_price = total_price - half
                user.CountBonus -= half
        elif user.Ref != 1 and off_bonus is False:
            count_bonus = int(total_price * 0.02)
            user.CountBonus += count_bonus
        await user_services.update_user(user_id, user)
        order = await order_services.create_order(Order(user_id=user_id, total_price=total_price))
        for bite in bouquets:
            orderboquets = await order_services.create_orderbouquets(OrderBouquets(order_id=order.ID,
                                                                                   bouquet_id=bite["bouquet"].ID,
                                                                                   quantity=bite["quantity"]))
    except Exception as ex:
        print(f"Error {ex}")
        raise HTTPException(status_code=500, detail=f"Order not created {ex}")


@app.get("/buy/history_order/", response_model=list[OrderHistory], tags=["Buy"])
async def buy_history_order(user_id):
    try:
        user = await user_services.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not exist")
        orders = await order_services.get_order_by_user_id(user_id)
        history = []
        for order in orders:
            orderbouquets = await order_services.get_orderbouquets_by_order_id(order.ID)
            orderhistory = OrderHistory(order_id=order.ID,
                                        user_id=order.UserID,
                                        date=order.Date,
                                        total_price=order.TotalPrice,
                                        bouquets=orderbouquets)
            history.append(orderhistory)
        return history
    except Exception as ex:
        print(f"Error {ex}")
        raise HTTPException(status_code=500, detail=f"Order not found {ex}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
