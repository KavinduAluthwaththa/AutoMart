from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from ..core.database import Base


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True) # e.g., ikman, patpat
    source_id = Column(String, index=True) # unique id at source
    title = Column(String, nullable=False)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    mileage = Column(Integer)
    price = Column(Float, index=True)
    currency = Column(String, default='LKR')
    details = Column(Text)
    url = Column(String)
    image_url = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())