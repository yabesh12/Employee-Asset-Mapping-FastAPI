# schema.py

from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID

class EmployeeCreate(BaseModel):
    """
    Pydantic model for creating a new employee.

    Attributes:
        - first_name (str): First name of the employee.
        - last_name (str): Last name of the employee.
        - gender (str): Gender of the employee.
        - phone_number (str): Phone number of the employee.
        - employee_email (str): Email address of the employee.
        - address (str): Address of the employee.
        - blood_group (str): Blood group of the employee.
        - emergency_contact_number (str): Emergency contact number of the employee.
    """
    first_name: str
    last_name: str
    gender: str
    phone_number: str
    employee_email: str
    address: str
    blood_group: str
    emergency_contact_number: str

class EmployeeUpdate(BaseModel):
    """
    Pydantic model for updating an existing employee.

    Attributes:
        - first_name (Optional[str]): Optional new first name of the employee.
        - last_name (Optional[str]): Optional new last name of the employee.
        - gender (Optional[str]): Optional new gender of the employee.
        - phone_number (Optional[str]): Optional new phone number of the employee.
        - employee_email (Optional[str]): Optional new email address of the employee.
        - address (Optional[str]): Optional new address of the employee.
        - blood_group (Optional[str]): Optional new blood group of the employee.
        - emergency_contact_number (Optional[str]): Optional new emergency contact number of the employee.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    employee_email: Optional[str] = None
    address: Optional[str] = None
    blood_group: Optional[str] = None
    emergency_contact_number: Optional[str] = None

class EmployeeResponse(EmployeeCreate):
    """
    Pydantic model for the response when creating or retrieving an employee.

    Attributes:
        - emp_id (uuid.UUID): UUID identifying the employee.
    """
    emp_id: UUID

class EmployeeListResponse(BaseModel):
    """
    Pydantic model for the response when retrieving a list of employees.

    Attributes:
        - employees (List[EmployeeResponse]): List of EmployeeResponse objects.
    """
    employees: List[EmployeeResponse]

class EmployeeID(BaseModel):
    """
    Pydantic model for an employee ID.

    Attributes:
        - employeeId (uuid.UUID): UUID identifying the employee.
    """
    employeeId: UUID

class SuccessResponse(BaseModel):
    """
    Pydantic model for a generic success response.

    Attributes:
        - success (bool): Indication of whether the operation was successful.
        - message (Optional[str]): Optional message providing additional information.
    """
    success: bool = True
    message: Optional[str] = None


class AssetCreate(BaseModel):
    """
    Pydantic model for creating a new asset.

    Attributes:
        - asset_name (str): Name of the asset.
        - asset_type (str): Type of the asset.
    """
    asset_name: str
    asset_type: str

class AssetUpdate(BaseModel):
    """
    Pydantic model for updating an existing asset.

    Attributes:
        - asset_name (Optional[str]): Updated name of the asset.
        - asset_type (Optional[str]): Updated type of the asset.
    """
    asset_name: Optional[str] = None
    asset_type: Optional[str] = None

class AssetResponse(BaseModel):
    """
    Pydantic model for the response when creating, updating, or retrieving an asset.

    Attributes:
        - asset_id (UUID): Unique identifier for the asset.
        - asset_name (str): Name of the asset.
        - asset_type (str): Type of the asset.
        - created_at (Optional[str]): Timestamp indicating the creation time.
        - updated_at (Optional[str]): Timestamp indicating the last update time.
    """
    asset_id: UUID
    asset_name: str
    asset_type: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AssetListResponse(BaseModel):
    """
    Pydantic model for the response when retrieving a list of assets.

    Attributes:
        - assets (List[AssetResponse]): List of assets.
    """
    assets: List[AssetResponse]


class AssetMappingCreate(BaseModel):
    """
    Pydantic model for creating an asset mapping.

    Attributes:
        - emp_id (UUID): Employee ID for mapping.
        - asset_id (UUID): Asset ID for mapping.
    """
    emp_id: UUID
    asset_id: UUID

class AssetMappingResponse(BaseModel):
    """
    Pydantic model for the response when creating, updating, or retrieving an asset mapping.

    Attributes:
        - id (UUID): Unique identifier for the mapping.
        - emp_id (UUID): Employee ID for mapping.
        - asset_id (UUID): Asset ID for mapping.
        - created_at (Optional[str]): Timestamp indicating the creation time.
        - updated_at (Optional[str]): Timestamp indicating the last update time.
    """
    id: UUID
    emp_id: UUID
    asset_id: UUID
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

class AssetMappingListResponse(BaseModel):
    """
    Pydantic model for the response when retrieving a list of asset mappings.

    Attributes:
        - mappings (List[AssetMappingResponse]): List of asset mappings.
    """
    mappings: List[AssetMappingResponse]

class AssetMappingID(BaseModel):
    """
    Pydantic model for the request when providing an asset mapping ID.

    Attributes:
        - mappingId (UUID): Asset mapping ID.
    """
    mappingId: UUID


class DashboardEmployee(BaseModel):
    """
    Pydantic model for representing employee details in the dashboard.

    Attributes:
        - emp_id (UUID): Employee ID.
        - first_name (str): First name of the employee.
        - last_name (str): Last name of the employee.
        - gender (str): Gender of the employee.
        - phone_number (str): Phone number of the employee.
        - employee_email (str): Email address of the employee.
        - address (str): Address of the employee.
        - blood_group (str): Blood group of the employee.
        - emergency_contact_number (str): Emergency contact number of the employee.
        - asset_count (int): Number of assets associated with the employee.
    """
    emp_id: UUID
    first_name: str
    last_name: str
    gender: str
    phone_number: str
    employee_email: str
    address: str
    blood_group: str
    emergency_contact_number: str
    asset_count: int

class DashboardResponse(BaseModel):
    """
    Pydantic model for the response when retrieving all employee details for the dashboard.

    Attributes:
        - EmployeeList (List[DashboardEmployee]): List of employee details.
    """
    EmployeeList: List[DashboardEmployee]