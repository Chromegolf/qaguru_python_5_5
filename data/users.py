from dataclasses import dataclass
from enum import Enum
from typing import List
from datetime import date


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    computer_science = 'Computer Science'
    english = 'English'


class Hobby(Enum):
    sport = 'Sports'
    reading = 'Reading'
    music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    gender: List[Gender]
    birthday: date
    subjects: List[Subject]
    hobbies: List[Hobby]
    upload_picture: str
    current_address: str
    state: str
    city: str

