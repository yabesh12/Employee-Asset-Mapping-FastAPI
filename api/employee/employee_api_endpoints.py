# routers/employee.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from uuid import UUID as PyUUID
from schema import EmployeeCreate, EmployeeUpdate, EmployeeResponse, EmployeeListResponse, SuccessResponse
from models import Employee
from settings import get_db

router = APIRouter()

@router.post("/createemployee", response_model=EmployeeResponse)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee.

    Args:
        - employee (EmployeeCreate): Pydantic model for creating a new employee.
        - db (Session): SQLAlchemy database session.

    Returns:
        EmployeeResponse: Pydantic model for the response when creating or retrieving an employee.
    """
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.put("/editemployee/{employeeId}", response_model=EmployeeResponse)
def edit_employee(employeeId: PyUUID, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    """
    Update an existing employee.

    Args:
        - employeeId (PyUUID): UUID identifying the employee.
        - employee (EmployeeUpdate): Pydantic model for updating an existing employee.
        - db (Session): SQLAlchemy database session.

    Returns:
        EmployeeResponse: Pydantic model for the response when creating or retrieving an employee.
    """
    db_employee = db.query(Employee).filter(Employee.emp_id == employeeId).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    for field, value in employee.dict(exclude_unset=True).items():
        setattr(db_employee, field, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

@router.delete("/deleteemployee/{employeeId}", response_model=SuccessResponse)
def delete_employee(employeeId: PyUUID, db: Session = Depends(get_db)):
    """
    Delete an employee.

    Args:
        - employeeId (PyUUID): UUID identifying the employee.
        - db (Session): SQLAlchemy database session.

    Returns:
        SuccessResponse: Pydantic model for a generic success response.
    """
    db_employee = db.query(Employee).filter(Employee.emp_id == employeeId).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(db_employee)
    db.commit()
    return {"success": True, "message": "Employee deleted successfully"}

@router.get("/getallemployee", response_model=EmployeeListResponse)
def get_all_employees(db: Session = Depends(get_db)):
    """
    Get a list of all employees.

    Args:
        - db (Session): SQLAlchemy database session.

    Returns:
        EmployeeListResponse: Pydantic model for the response when retrieving a list of employees.
    """
    employees = db.query(Employee).all()
    return {"employees": employees}


@router.get("/getemployee/{employeeId}", response_model=EmployeeResponse)
def get_employee(employeeId: PyUUID, db: Session = Depends(get_db)):
    """
    Get details of a specific employee.

    Args:
        - employeeId (PyUUID): UUID identifying the employee.
        - db (Session): SQLAlchemy database session.

    Returns:
        EmployeeResponse: Pydantic model for the response when creating or retrieving an employee.
    """
    db_employee = db.query(Employee).filter(Employee.emp_id == employeeId).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee