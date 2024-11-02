from dataclasses import dataclass


@dataclass
class CreateUser:
    email: str
    first_name: str
    last_name: str
    phone_number: str
    password: str
