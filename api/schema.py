from pydantic import BaseModel
from datetime import date, time, datetime
from typing import List

class UserBase(BaseModel):
    first_name: str
    middle_name: str
    surname: str
    cellphone: str
    email: str
    gender: str
    city: str
    state: str
    zipcode: str
    timezone: str

class UserCreate(UserBase):
    password: str

class UserResult(UserBase):
    id: int

    class Config:
        orm_mode = True

class ParticipantBase(BaseModel):
    participant_id: int
    meeting_id: int

class ParticipantResult(ParticipantBase):
    class Config:
        orm_mode = True

class AvailabilityBase(BaseModel):
    start_date: date
    end_date: date
    reason: str
    users_id: int

class AvailabilityResult(AvailabilityBase):
    id: int

    class Config:
        orm_mode = True

class MeetingBase(BaseModel):
    title: str
    date: date
    time: time
    organizer: int

class MeetingResult(MeetingBase):
    id: int

    class Config:
        orm_mode = True

class Meetings(BaseModel):
    meeting_id: int
    title: str
    date: str
    time: str
    organizer: str
    participants: List[UserResult] = []

class UserMeetings(BaseModel):
    first_name: str
    email: str
    gender: str
    city: str
    state: str
    timezone: str
    hosts: List[Meetings] = []
    participants: List[Meetings] = []
