from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from ..core.database import Base


class PriceHistory(Base):
    __tablename__ = 'price_history'
    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id', ondelete='CASCADE'), index=True)
    price = Column(Float, nullable=False)
    currency = Column(String, default='LKR')
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())