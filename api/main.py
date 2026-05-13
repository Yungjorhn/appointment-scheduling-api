from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from api.config.database import SessionLocal
from api.schema import UserCreate, UserResult, UserMeetings, AvailabilityBase, AvailabilityResult, ParticipantBase, ParticipantResult, MeetingResult, MeetingBase
from api.crud import User as crud_user
from api.crud import Leave as crud_availability
from api.crud import Participant as crud_participant
from api.crud import Meeting as crud_meeting

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users", response_model=List[UserResult])
def get_all_users(db: Session=Depends(get_db)):
    return crud_user.get_all(db)

@app.post("/users", response_model=UserResult)
def create_user(user:UserCreate, db: Session = Depends(get_db)):
    existing_user = crud_user.get_by_email(db, email=user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.add(db, user=user)

@app.get("/users/{user_id}", response_model=UserResult)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/email/{email}", response_model=UserResult)
def get_user_by_email(email:str, db: Session = Depends(get_db)):
    db_user = crud_user.get_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/{user_id}/meetings", response_model=UserMeetings)
def get_user_meetings(user_id:int, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    meetings = crud_user.getMeetingInfo(db, user_id = user_id)
    return meetings


@app.get("/availabilities", response_model=AvailabilityResult)
def get_all_availabilities(db: Session = Depends(get_db)):
    return crud_availability.get_all(db)

@app.post("/leave", response_model=AvailabilityResult)
def create_availability(availability: AvailabilityBase, db: Session = Depends(get_db)):
    return crud_availability.add(db, availability = availability)

@app.get("/availabilities", response_model= AvailabilityResult)
def get_availability(id: int, db: Session = Depends(get_db)):
    db_availability = crud_availability.get(db, id = id)
    if db_availability is None:
        raise HTTPException(status_code=404, detail="Availability not found")
    return db_availability

@app.get("/participants", response_model=List[ParticipantResult])
def get_all_participant(db: Session = Depends(get_db)):
    return crud_participant.get_all()

@app.post("/participants", response_model=ParticipantResult)
def create_participant(participant: ParticipantBase, db: Session = Depends(get_db)):
    return crud_participant.add(db, participant=participant)

@app.get("/participants/{participant_id}/{meeting_id}", response_model=ParticipantResult)
def get_participant(participant_id:int, meeting_id: int, db: Session = Depends(get_db)):
    db_participant = crud_participant.get(db, participant_id=participant_id, meeting_id = meeting_id)
    if db_participant is None:
        raise HTTPException(status_code=404, detail= "Participant record not found")
    return db_participant

@app.get("/user/{user_id}/participants-meetings", response_model=List[MeetingResult])
def get_user_participation(user_id: int, db: Session = Depends(get_db)):
    return crud_participant.get_meetings(db, user_id = user_id)

@app.get("/meetings/{meeting_id}/participants", response_model = List[UserResult])
def get_meeting_participants(meeting_id: int, db: Session = Depends(get_db)):
    return crud_participant.participants_by_meetings(db, meeting_id = meeting_id)

@app.get("/meetings", response_model = List[MeetingResult])
def get_all_meeting(db: Session = Depends(get_db)):
    return crud_meeting.get_all(db)

@app.post("/meetings", response_model = MeetingResult)
def create_meeting(meeting: MeetingBase, db: Session = Depends(get_db)):
    return crud_meeting.add(db, meeting)

@app.get("/meetings/{meeting_id}", response_model = MeetingResult)
def get_meeting(meeting_id: int, db: Session = Depends(get_db)):
    db_meeting = crud_meeting.get(db, meeting_id)
    if db_meeting is None:
        raise HTTPException(status_code = 404, detail = "Meeting not found")
    return db_meeting

