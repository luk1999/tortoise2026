from http import HTTPStatus

from errors import ForbiddenError
from fastapi import APIRouter, Response
from services.users import BaseUserCreate, UserError, UserService

router = APIRouter(prefix="/users")


@router.get("/")
async def get_users():
    return await UserService.get_all()


@router.get("/{user_id}")
async def get_user(user_id: int):
    return await UserService.get(user_id)


@router.post("/", status_code=HTTPStatus.CREATED)
async def add_user(user: BaseUserCreate):
    await UserService.add(user)
    return {"detail": "Created"}


@router.post("/activate", status_code=HTTPStatus.ACCEPTED)
async def activate_user(username: str):
    try:
        await UserService.activate(username)
    except UserError as error:
        raise ForbiddenError(str(error)) from error
    return {"detail": "Activated"}


@router.post("/deactivate", status_code=HTTPStatus.ACCEPTED)
async def deactivate_user(username: str):
    try:
        await UserService.deactivate(username)
    except UserError as error:
        raise ForbiddenError(str(error)) from error
    return {"detail": "Deactivated"}


@router.get(".txt")
async def get_user_names():
    users = await UserService.get_all()
    return Response(content="\n".join(user.username for user in users), media_type="text")
