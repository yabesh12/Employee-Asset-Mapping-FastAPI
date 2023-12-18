# models.py

from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, func, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import uuid
from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimestampModel(Base):
    """
    Abstract base class for models with timestamp columns.

    Attributes:
        created_at (DateTime): Timestamp indicating the creation time.
        updated_at (DateTime): Timestamp indicating the last update time.
    """
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class Employee(TimestampModel):
    """
    Employee model representing the 'employees' table.

    Attributes:
        emp_id (UUID): Primary key, UUID for employee identification.
        first_name (str): First name of the employee.
        last_name (str): Last name of the employee.
        gender (str): Gender of the employee.
        phone_number (str): Phone number of the employee.
        employee_email (str): Email address of the employee.
        address (str): Address of the employee.
        blood_group (str): Blood group of the employee.
        emergency_contact_number (str): Emergency contact number of the employee.
        assets (relationship): Relationship to the EmployeeAssetMapping table.
    """

    __tablename__ = 'employees'

    emp_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    employee_email = Column(String, nullable=False, unique=True)
    address = Column(Text, nullable=False)
    blood_group = Column(String, nullable=False)
    emergency_contact_number = Column(String, nullable=False)
    assets = relationship("EmployeeAssetMapping", back_populates="employee")

    def calculate_asset_count(self, session):
        """
        Calculate the number of assets associated with the employee.

        Args:
            session (Session): SQLAlchemy session object.

        Returns:
            int: Number of assets associated with the employee.
        """
        return session.query(func.count(EmployeeAssetMapping.id)).filter_by(emp_id=self.emp_id).scalar()


class Asset(TimestampModel):
    """
    Asset model representing the 'assets' table.

    Attributes:
        asset_id (UUID): Primary key, UUID for asset identification.
        asset_name (str): Name of the asset.
        asset_type (str): Type of the asset.
        employees (relationship): Relationship to the EmployeeAssetMapping table.
    """

    __tablename__ = 'assets'

    asset_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    asset_name = Column(String, nullable=False)
    asset_type = Column(String, nullable=False)
    employees = relationship("EmployeeAssetMapping", back_populates="asset")


class EmployeeAssetMapping(TimestampModel):
    """
    EmployeeAssetMapping model representing the 'employee_asset_mapping' table.

    Attributes:
        id (UUID): Primary key, UUID for mapping identification.
        emp_id (UUID): Foreign key, UUID referencing employees table.
        asset_id (UUID): Foreign key, UUID referencing assets table.
        employee (relationship): Relationship to the Employee table.
        asset (relationship): Relationship to the Asset table.
    """

    __tablename__ = 'employee_asset_mapping'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    emp_id = Column(UUID(as_uuid=True), ForeignKey('employees.emp_id'), nullable=False)
    asset_id = Column(UUID(as_uuid=True), ForeignKey('assets.asset_id'), nullable=False)
    employee = relationship("Employee", back_populates="assets")
    asset = relationship("Asset", back_populates="employees")
