from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from api.config.database import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    organizer = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    participants = relationship("Participant", cascade="all, delete-orphan")