from fastapi import APIRouter
from pydantic import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("", status_code=201)
def create_user(request: CreateUserRequest):
    user_service = UserService() # TODO: inject dependency
    created_user = user_service.create_user(
        name=request.name,
        email=request.email,
        password=request.password,
    )
    return created_user