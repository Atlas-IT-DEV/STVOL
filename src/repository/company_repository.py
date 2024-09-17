from src.database.my_connector import Database
from src.database.models import CompanyData
from src.database.my_connector import db


def get_all_companys():
    query = "SELECT * FROM сompany_Data"
    return db.fetch_all(query)


def get_company_by_id(company_id: int):
    query = "SELECT * FROM сompany_Data WHERE id=%s"
    return db.fetch_one(query, (company_id,))


def create_company(company: CompanyData):
    query = "INSERT INTO сompany_Data (name, description) VALUES (%s, %s)"
    params = (company.Name, company.Disc)
    cursor = db.execute_query(query, params)
    return cursor.lastrowid


def update_company(company_id: int, company: CompanyData):
    query = "UPDATE сompany_Data SET name=%s, description=%s WHERE id=%s"
    params = (company.Name, company.Disc, company_id)
    db.execute_query(query, params)


def delete_company(company_id: int):
    query = "DELETE FROM сompany_Data WHERE id=%s"
    db.execute_query(query, (company_id,))
