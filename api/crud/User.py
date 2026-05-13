from sqlalchemy.orm import Session
from api.models.User import User
from api.models.Meeting import Meeting
from api.models.Participants import Participant
from api.schema import UserCreate

def get_all(db:Session):
    return db.query(User).all()

def add(db:Session, user:UserCreate):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db:Session, id:int):
    return db.query(User).filter(User.id == id).first()

def get_by_email(db:Session, email:str):
    return db.query(User).filter(User.email == email).first()

def getMeetingInfo(db:Session, user_id:int):
    return db.query(Meeting).join(Participant).filter(Participant.participant_id == user_id).all()


