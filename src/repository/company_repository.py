from src.database.my_connector import Database
from src.database.models import CompanyData
db = Database()


async def get_all_companys():
    query = "SELECT * FROM Company_Data"
    return await db.fetch_all(query)


async def get_company_by_id(company_id: int):
    query = "SELECT * FROM Company_Data WHERE id=%s"
    return await db.fetch_one(query, (company_id,))


async def create_company(company: CompanyData):
    query = "INSERT INTO Company_Data (name, description) VALUES (%s, %s)"
    params = (company.Name, company.Disc)
    cursor = await db.execute_query(query, params)
    return cursor.lastrowid


async def update_company(company_id: int, company: CompanyData):
    query = "UPDATE Company_Data SET name=%s, description=%s WHERE id=%s"
    params = (company.Name, company.Disc, company_id)
    await db.execute_query(query, params)


async def delete_company(company_id: int):
    query = "DELETE FROM Company_Data WHERE id=%s"
    await db.execute_query(query, (company_id,))
