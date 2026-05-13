from sqlalchemy.orm import Session
from api.models.Meeting import Meeting
from api.schema import MeetingBase

def get_all(db: Session):
    return db.query(Meeting).all()

def add(db: Session, meeting: MeetingBase):
    new_meeting = Meeting(**meeting.model_dump())
    db.add(new_meeting)
    db.commit()
    db.refresh(new_meeting)
    return new_meeting

def get(db: Session, meeting_id: int):
    return db.query(Meeting).filter(Meeting.id == meeting_id).first()


