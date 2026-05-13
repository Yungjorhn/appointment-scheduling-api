from sqlalchemy.orm import Session
from api.models.Availability import Availability
from api.schema import AvailabilityBase

def get_all(db: Session):
    return db.query(Availability).all()

def add(db: Session, availability: AvailabilityBase):
    new_availability = Availability(**availability.model_dump())
    db.add(new_availability)
    db.commit()
    db.refresh(new_availability)
    return new_availability

def get(db: Session, id: int):
    return db.query(Availability).filter(Availability.id == id).first()

