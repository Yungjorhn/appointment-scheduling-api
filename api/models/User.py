from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.config.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    cellphone = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    zipcode = Column(String, nullable=True)
    timezone = Column(String, nullable=False)

    availability = relationship("Availability", cascade="all, delete-orphan")
    meeting = relationship("Meeting", cascade="all, delete-orphan")
    participant = relationship("Participant", cascade="all, delete-orphan")