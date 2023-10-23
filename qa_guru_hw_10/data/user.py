from dataclasses import dataclass


@dataclass
class User:
    full_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state_and_city: str


