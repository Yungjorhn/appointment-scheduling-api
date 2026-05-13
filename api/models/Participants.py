from sqlalchemy import Column, Integer, ForeignKey
from api.config.database import Base

class Participant(Base):
    __tablename__ = "participants"

    participant_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id", ondelete="CASCADE"), primary_key=True)