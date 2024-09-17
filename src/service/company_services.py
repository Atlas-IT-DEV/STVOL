from src.repository import company_repository
from src.database.models import CompanyData
from fastapi import HTTPException, status
from src.utils.exam_services import check_if_exists, check_for_duplicates


def get_all_companys():
    companys = company_repository.get_all_companys()
    return [CompanyData(**company) for company in companys]


def get_company_by_id(company_id: int):
    company = company_repository.get_company_by_id(company_id)
    if not company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Company not found')
    return CompanyData(**company) if company else None


def create_company(company: CompanyData):
    check_if_exists(
        get_all=get_all_companys,
        attr_name="Name",
        attr_value=company.Name,
        exception_detail='Name already exist'
    )
    company_id = company_repository.create_company(company)
    return get_company_by_id(company_id)


def update_company(company_id: int, company: CompanyData):
    check_for_duplicates(
        get_all=get_all_companys,
        check_id=company_id,
        attr_name="Name",
        attr_value=company.Name,
        exception_detail='Name already exist'
    )
    company_repository.update_company(company_id, company)
    return {"message": "Company updated successfully"}


def delete_company(company_id: int):
    get_company_by_id(company_id)
    company_repository.delete_company(company_id)
    return {"message": "Company deleted successfully"}
