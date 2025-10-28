import re
from sqlmodel import Field
from pydantic import BaseModel
from pydantic import EmailStr, field_validator

class UserRegister(BaseModel):
    """Schema for user registration"""
    first_name: str = Field(min_length=1, max_length=64, title="First name")
    last_name: str = Field(min_length=1, max_length=64, title="Last name")
    email : EmailStr = Field(min_length=1, max_length=64, title="Email")
    username: str = Field(min_length=1, max_length=64, title="Username")
    phone_number: str = Field(min_length=1, max_length=64, title="Phone number")
    date_of_birth: str = Field(min_length=1, max_length=64, title="Date of birth")
    avatar_url: str = Field(min_length=1, max_length=64, title="Avatar URL")
    bio : str= Field(min_length=1, max_length=256, title="Bio")
    password: str = Field(min_length=8, max_length=128)
    confirm_password: str = Field(min_length=8, max_length=128)

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        """Password strength validation"""
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        if len(v) > 128:
            raise ValueError('Password must be less than 128 characters')

        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one digit')
        if not re.search(r'[A-Za-z]', v):
            raise ValueError('Password must contain at least one letter')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', v):
            raise ValueError(
                'Password must contain at least one special character')
        return v

    @field_validator('confirm_password')
    @classmethod
    def passwords_match(cls, v: str, info) -> str:
        """Validate passwords match"""
        if 'password' in info.data and v != info.data['password']:
            raise ValueError('Passwords do not match')
        return v


class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str = Field(min_length=1)
