from src.repository import company_repository
from src.database.models import CompanyData


def get_all_companys():
    companys = company_repository.get_all_companys()
    return [CompanyData(**company) for company in companys]


def get_company_by_id(company_id: int):
    company = company_repository.get_company_by_id(company_id)
    return CompanyData(**company) if company else None


def create_company(company: CompanyData):
    company_id = company_repository.create_company(company)
    return get_company_by_id(company_id)


def update_company(company_id: int, company: CompanyData):
    company_repository.update_company(company_id, company)
    return {"message": "Company updated successfully"}


def delete_company(company_id: int):
    company_repository.delete_company(company_id)
    return {"message": "Company deleted successfully"}
