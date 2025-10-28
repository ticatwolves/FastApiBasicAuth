from fastapi import APIRouter
from fastapi_basic_auth.schemas.user import UserRegister, UserLogin

users_router = APIRouter()


@users_router.post("/register/", tags=["users"])
async def register(user: UserRegister):
    """
    User registration API
    """
    print(user)
    return {}

@users_router.post("/login/", tags=["users"])
async def read_users(user: UserLogin):
    """
    User login API
    """
    print(user)
    return {}

