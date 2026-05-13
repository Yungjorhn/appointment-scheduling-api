from sqlalchemy.orm import Session
from api.models.Participants import Participant
from api.schema import ParticipantBase
from api.models.User import User
from api.models.Meeting import Meeting

def get_all(db: Session):
    return db.query(Participant).all()

def add(db: Session, participant: ParticipantBase):
    new_participant = Participant(**participant.model_dump())
    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)
    return new_participant

def get(db: Session, participant_id: int, meeting_id: int):
    return db.query(Participant).filter(Participant.participant_id == participant_id, Participant.meeting_id == meeting_id).first()

def get_meetings(db: Session, user_id: int):
    return db.query(Meeting).join(Participant).filter(Participant.participant_id == user_id).all()

def participants_by_meetings(db: Session, meeting_id: int):
    return db.query(User).join(Participant).filter(Participant.meeting_id==meeting_id).all()