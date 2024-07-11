from fastapi import FastAPI, HTTPException, Header
from src.database.my_connector import Database
from typing import Dict
from fastapi.openapi.models import Tag
from fastapi.middleware.cors import CORSMiddleware
from src.service import user_services, adress_services, order_services, bouquet_services, company_services
from src.database.models import User, Adress, Order, Bouquet, CompanyData

db = Database()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Определяем теги
TestTag = Tag(name="Test", description="Маршрут для тестирования")
BonusTag = Tag(name="Bonus", description="Расчет бонусов пользователя")
UserTag = Tag(name="User", description="CRUD операции пользователь")
AdressTag = Tag(name="Adress", description="CRUD операции адресс")
OrderTag = Tag(name="Order", description="CRUD операции заказ")
BouquetTag = Tag(name="Bouquet", description="CRUD операции букет")
CompanyTag = Tag(name="Company", description="CRUD операции компании")

# Настройка документации с тегами
app.openapi_tags = [
    TestTag.dict(),
    BonusTag.dict(),
    UserTag.dict(),
    AdressTag.dict(),
    OrderTag.dict(),
    BouquetTag.dict(),
    CompanyTag.dict()
]


@app.on_event("startup")
async def startup_event():
    connected = await db.connect()
    if not connected:
        await db.check_and_reconnect()


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
    existing_user = await get_user_by_phone(user.Phone)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exist")
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


@app.post("/bouquets/", response_model=Bouquet, tags=["Bouquet"])
async def create_bouquet(bouquet: Bouquet):
    return await bouquet_services.create_bouquet(bouquet)


@app.put("/bouquets/{bouquet_id}", response_model=Dict, tags=["Bouquet"])
async def update_bouquet(bouquet_id, bouquet: Bouquet):
    return await bouquet_services.update_bouquet(bouquet_id, bouquet)


@app.delete("/bouquets/bouquet_id}", response_model=Dict, tags=["Bouquet"])
async def delete_bouquet(bouquet_id):
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


@app.delete("/companys/company_id}", response_model=Dict, tags=["Company"])
async def delete_company(company_id):
    return await company_services.delete_company(company_id)


@app.get("/bonus/order/{order_id]", response_model=Order, tags=["Bonus"])
async def completed_order(order_id: int):
    order = await order_services.get_order_by_id(order_id)
    order.Completed = 1
    await order_services.update_order(order_id, order)
    new_order = await order_services.get_order_by_id(order_id)
    return new_order


@app.get("/bonus/user/{user_id}", response_model=User, tags=["Bonus"])
async def bonus(user_id: int):
    orders = await order_services.get_order_by_user_id(user_id)
    if not orders:
        raise HTTPException(status_code=404, detail="User not do orders yet")
    bonuses = []
    for order in orders:
        if order.Completed == 1:
            bonuses.append(int(order.Price * 2 / 100))
    bonus = sum(bonuses)
    user = await user_services.get_user_by_id(user_id)
    user.CountBonus = bonus
    await user_services.update_user(user_id, user)
    new_user = await user_services.get_user_by_id(user_id)
    return new_user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
