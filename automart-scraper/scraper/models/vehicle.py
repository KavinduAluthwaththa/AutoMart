from dataclasses import dataclass
from typing import Optional


@dataclass
class Vehicle:
    source: str
    source_id: str
    title: str
    make: Optional[str] = None
    model: Optional[str] = None
    year: Optional[int] = None
    mileage: Optional[int] = None
    price: Optional[float] = None
    currency: Optional[str] = 'LKR'
    url: Optional[str] = None
    image_url: Optional[str] = None
    details: Optional[str] = None

    # New fields from screenshot
    body_style: Optional[str] = None
    model_year: Optional[str] = None
    condition: Optional[str] = None
    reference_no: Optional[str] = None
    transmission: Optional[str] = None
    engine_cylinders: Optional[str] = None
    fuel: Optional[str] = None
    doors: Optional[int] = None
    exterior_color: Optional[str] = None
    interior_color: Optional[str] = None
    comfort: Optional[dict] = None
    sound_system: Optional[dict] = None
    safety: Optional[dict] = None
    windows: Optional[dict] = None
    additional_info: Optional[str] = None

    def to_dict(self):
        return {
            "source": self.source,
            "source_id": self.source_id,
            "title": self.title,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
            "price": self.price,
            "currency": self.currency,
            "url": self.url,
            "image_url": self.image_url,
            "details": self.details,
            "body_style": self.body_style,
            "model_year": self.model_year,
            "condition": self.condition,
            "reference_no": self.reference_no,
            "transmission": self.transmission,
            "engine_cylinders": self.engine_cylinders,
            "fuel": self.fuel,
            "doors": self.doors,
            "exterior_color": self.exterior_color,
            "interior_color": self.interior_color,
            "comfort": self.comfort,
            "sound_system": self.sound_system,
            "safety": self.safety,
            "windows": self.windows,
            "additional_info": self.additional_info,
        }
    
    