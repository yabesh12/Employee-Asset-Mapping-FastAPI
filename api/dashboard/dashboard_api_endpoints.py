# main.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import DashboardResponse
from models import Employee, EmployeeAssetMapping
from settings import get_db
from sqlalchemy import func 

router = APIRouter()

@router.get("/dashboard/getdetails", response_model=DashboardResponse)
def get_all_employee_details(db: Session = Depends(get_db)):
    """
    Get all employee details for the dashboard.

    Args:
        - db (Session): SQLAlchemy database session.

    Returns:
        DashboardResponse: Pydantic model for the response when retrieving all employee details for the dashboard.
    """
    query = (
        db.query(Employee, func.count(EmployeeAssetMapping.id).label("asset_count"))
        .outerjoin(EmployeeAssetMapping, Employee.emp_id == EmployeeAssetMapping.emp_id)
        .group_by(Employee.emp_id)
    )
    employee_details = [
        {
            "emp_id": emp.emp_id,
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "gender": emp.gender,
            "phone_number": emp.phone_number,
            "employee_email": emp.employee_email,
            "address": emp.address,
            "blood_group": emp.blood_group,
            "emergency_contact_number": emp.emergency_contact_number,
            "asset_count": asset_count,
        }
        for emp, asset_count in query.all()
    ]
    return {"EmployeeList": employee_details}
