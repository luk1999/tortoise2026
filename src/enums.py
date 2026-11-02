from enum import StrEnum


class Genre(StrEnum):
    adventure = "adventure"
    autobiography = "autobiography"
    biography = "biography"
    fantasy = "fantasy"
    history = "history"
    horror = "horror"
    mystery = "mystery"
    poetry = "poetry"
    romance = "romance"
    sci_fi = "sci_fi"
    thriller = "thriller"


class UserStatus(StrEnum):
    INACTIVE = "inactive"
    ACTIVE = "active"
    DELETED = "deleted"


class UserAction(StrEnum):
    LOGIN = "login"
    LOGOUT = "logout"
