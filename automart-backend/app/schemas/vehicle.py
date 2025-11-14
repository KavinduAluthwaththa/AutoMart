from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class VehicleBase(BaseModel):
    title: str
    make: Optional[str]
    model: Optional[str]
    year: Optional[int]
    mileage: Optional[int]
    price: Optional[float]
    currency: Optional[str]
    url: Optional[str]
    image_url: Optional[str]


class VehicleCreate(VehicleBase):
    source: str
    source_id: str


class Vehicle(VehicleBase):
    id: int
    created_at: datetime
    updated_at: datetime


class Config:
    orm_mode = True