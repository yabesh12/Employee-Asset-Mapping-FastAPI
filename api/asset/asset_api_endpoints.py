from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema import AssetCreate, AssetUpdate, AssetResponse, AssetListResponse, SuccessResponse
from models import Asset
from settings import get_db
from uuid import UUID as PyUUID

router = APIRouter()

@router.post("/createasset", response_model=AssetResponse)
def create_asset(asset: AssetCreate, db: Session = Depends(get_db)):
    """
    Create a new asset.

    Args:
        - asset (AssetCreate): Pydantic model for creating a new asset.
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetResponse: Pydantic model for the response when creating or retrieving an asset.
    """
    db_asset = Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.put("/editasset/{assetid}", response_model=AssetResponse)
def edit_asset(assetid: PyUUID, asset: AssetUpdate, db: Session = Depends(get_db)):
    """
    Update an existing asset.

    Args:
        - assetid (UUID): UUID identifying the asset.
        - asset (AssetUpdate): Pydantic model for updating an existing asset.
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetResponse: Pydantic model for the response when creating or retrieving an asset.
    """
    db_asset = db.query(Asset).filter(Asset.asset_id == assetid).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    for field, value in asset.dict(exclude_unset=True).items():
        setattr(db_asset, field, value)
    db.commit()
    db.refresh(db_asset)
    return db_asset

@router.delete("/deleteasset/{assetId}", response_model=SuccessResponse)
def delete_asset(assetId: PyUUID, db: Session = Depends(get_db)):
    """
    Delete an asset.

    Args:
        - assetId (UUID): UUID identifying the asset.
        - db (Session): SQLAlchemy database session.

    Returns:
        SuccessResponse: Pydantic model for a generic success response.
    """
    db_asset = db.query(Asset).filter(Asset.asset_id == assetId).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    db.delete(db_asset)
    db.commit()
    return {"success": True, "message": "Asset deleted successfully"}

@router.get("/getallasset", response_model=AssetListResponse)
def get_all_assets(db: Session = Depends(get_db)):
    """
    Get a list of all assets.

    Args:
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetListResponse: Pydantic model for the response when retrieving a list of assets.
    """
    assets = db.query(Asset).all()
    return {"assets": assets}


@router.get("/getasset/{assetId}", response_model=AssetResponse)
def get_single_asset(assetId: PyUUID, db: Session = Depends(get_db)):
    """
    Get details of a specific asset.

    Args:
        - assetId (UUID): UUID identifying the asset.
        - db (Session): SQLAlchemy database session.

    Returns:
        AssetResponse: Pydantic model for the response when creating or retrieving an asset.
    """
    db_asset = db.query(Asset).filter(Asset.asset_id == assetId).first()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset