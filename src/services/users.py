import hashlib

from entities import BaseUser, BaseUserWithBooks
from enums import UserStatus
from errors import ConflictError, DoesNotExistError
from models import User
from pydantic import BaseModel, field_validator
from tortoise.exceptions import DoesNotExist

MIN_PASS_LEN = 8


def encode_password(password: str) -> str:
    """
    Demo-only password hashing. Do not use for production!!!
    """
    return hashlib.md5(password.encode()).hexdigest()


class UserError(Exception): ...


class UserCannotBeActivatedError(UserError): ...


class UserCannotBeDisabledError(UserError): ...


class BaseUserCreate(BaseModel):
    username: str
    first_name: str | None = None
    last_name: str | None = None
    password: str

    @field_validator("password")
    @classmethod
    def password_validator(cls, password: str) -> str:
        if not password or len(password) < MIN_PASS_LEN:
            raise ValueError(f"Password must have at least {MIN_PASS_LEN} chars")
        return encode_password(password)


class UserService:
    encode_password = staticmethod(encode_password)

    @staticmethod
    async def get_all() -> tuple[BaseUser]:
        users = await User.all()
        return tuple([await BaseUser.from_tortoise_orm(user) for user in users])

    @staticmethod
    async def get(user_id: int) -> BaseUserWithBooks:
        try:
            user = await User.get(id=user_id).prefetch_related("books")
            return await BaseUserWithBooks.from_tortoise_orm(user)
        except DoesNotExist as error:
            raise DoesNotExistError from error

    @staticmethod
    async def add(user: BaseUserCreate) -> BaseUser:
        if await User.filter(username=user.username).exists():
            raise ConflictError("User already exists")

        created_user = await User.create(**user.model_dump())
        return await BaseUser.from_tortoise_orm(created_user)

    @staticmethod
    async def activate(username: str) -> None:
        try:
            user = await User.get(username__iexact=username)
        except DoesNotExist as error:
            raise DoesNotExistError from error

        if user.status != UserStatus.INACTIVE:
            raise UserCannotBeActivatedError("User cannot be activated")

        user.status = UserStatus.ACTIVE
        await user.save(update_fields=("status",))

    @staticmethod
    async def deactivate(username: str) -> None:
        try:
            user = await User.get(username__iexact=username)
        except DoesNotExist as error:
            raise DoesNotExistError from error

        if user.status != UserStatus.ACTIVE:
            raise UserCannotBeDisabledError("User cannot be disabled")

        user.status = UserStatus.DELETED
        await user.save(update_fields=("status",))
