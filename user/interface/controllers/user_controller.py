from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependency_injector.wiring import inject, Provide
from containers import Container

from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.post("", status_code=201)
@inject
def create_user(
    request: CreateUserRequest,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    created_user = user_service.create_user(
        name=request.name,
        email=request.email,
        password=request.password,
    )
    return created_user

class UpdateUserRequest(BaseModel):
    name: str | None = None
    password: str | None = None

@router.put("/{user_id}")
@inject
def update_user(
    user_id: str,
    request: UpdateUserRequest,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    updated_user = user_service.update_user(
        user_id=user_id,
        name=request.name,
        password=request.password
    )

    return updated_user

@router.get("")
@inject
def get_users(
    page: int = 1,
    size: int = 10,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    total_count, users = user_service.get_users(page, size)

    return {
        "total_count": total_count,
        "page": page,
        "users": users
    }

@router.delete("/{user_id}", status_code=204)
@inject
def delete_user(
    user_id: str,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    # TODO authorization: 다른 유저를 삭제할 수 없도록 토큰에서 유저 아이디를 구한다.
    user_service.delete_user(user_id)