# main.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import AssetMappingCreate, AssetMappingResponse, AssetMappingListResponse, AssetMappingID
from models import EmployeeAssetMapping, Asset
from settings import get_db
from uuid import UUID

router = APIRouter()

@router.post("/mapping/assignassetmapping", response_model=AssetMappingResponse)
def assign_asset_mapping(mapping: AssetMappingCreate, db: Session = Depends(get_db)):
    """
    Assign an asset mapping to an employee.

    Args:
        - mapping (AssetMappingCreate): Pydantic model for creating an asset mapping.
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetMappingResponse: Pydantic model for the response when creating an asset mapping.
    """
    db_mapping = EmployeeAssetMapping(**mapping.dict())
    db.add(db_mapping)
    db.commit()
    db.refresh(db_mapping)
    return db_mapping

@router.get("/mapping/getallassets/{employeeId}", response_model=AssetMappingListResponse)
def get_all_assets_mapped(employeeId: UUID, db: Session = Depends(get_db)):
    """
    Get all assets mapped to a specific employee.

    Args:
        - employeeId (UUID): Employee ID.
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetMappingListResponse: Pydantic model for the response when retrieving a list of asset mappings.
    """
    mappings = db.query(EmployeeAssetMapping).filter(EmployeeAssetMapping.emp_id == employeeId).all()
    return {"mappings": mappings}

@router.delete("/mapping/removeassetmapping/{mappingId}", response_model=AssetMappingID)
def remove_asset_mapping(mappingId: UUID, db: Session = Depends(get_db)):
    """
    Remove an asset mapping.

    Args:
        - mappingId (UUID): Asset mapping ID.
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetMappingID: Pydantic model for the request when providing an asset mapping ID.
    """
    db_mapping = db.query(EmployeeAssetMapping).filter(EmployeeAssetMapping.id == mappingId).first()
    if db_mapping is None:
        raise HTTPException(status_code=404, detail="Asset mapping not found")
    db.delete(db_mapping)
    db.commit()
    return {"mappingId": mappingId}
