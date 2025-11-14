from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...core.database import get_db
from ...schemas.vehicle import Vehicle, VehicleCreate
from ...models.vehicle import Vehicle as VehicleModel


router = APIRouter(prefix="/cars", tags=["cars"])


@router.post("/", response_model=Vehicle)
def create_vehicle(payload: VehicleCreate, db: Session = Depends(get_db)):
	# upsert logic: try find by source+source_id
	existing = db.query(VehicleModel).filter(
		VehicleModel.source == payload.source,
		VehicleModel.source_id == payload.source_id
	).first()
	if existing:
		# update fields
		for k, v in payload.dict(exclude_unset=True).items():
			setattr(existing, k, v)
		db.add(existing)
		db.commit()
		db.refresh(existing)
		return existing

	obj = VehicleModel(**payload.dict())
	db.add(obj)
	db.commit()
	db.refresh(obj)
	return obj


@router.get("/", response_model=list[Vehicle])
def list_vehicles(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
	return db.query(VehicleModel).offset(skip).limit(limit).all()