from sqlalchemy import Column, Integer, String, Date, ForeignKey
from api.config.database import Base

class Availability(Base):
    __tablename__ = "availabilities"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    reason = Column(String, nullable=True)
    users_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)