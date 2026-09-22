from enums import Genre, UserStatus
from tortoise import Tortoise, fields
from tortoise.models import Model


class Author(Model):
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    date_of_birth = fields.DateField()

    class Meta:
        unique_together = (("first_name", "last_name", "date_of_birth"),)


class Book(Model):
    author = fields.ForeignKeyField("models.Author", related_name="books", on_delete=fields.CASCADE)
    title = fields.CharField(max_length=100)
    year = fields.IntField()
    genre = fields.CharEnumField(enum_type=Genre)

    class Meta:
        unique_together = (("author", "title"),)


class User(Model):
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=32)
    first_name = fields.CharField(max_length=100, null=True)
    last_name = fields.CharField(max_length=100, null=True)
    status = fields.CharEnumField(enum_type=UserStatus, default=UserStatus.INACTIVE)
    books = fields.ManyToManyField("models.Book", related_name="users")


def init_tortoise(app) -> None:
    """Example hook for application startup. This is intentionally lightweight.

    Use it in your main app setup to initialize Tortoise ORM.
    """

    Tortoise.init_models(["models"], "models")
    app.state.tortoise = Tortoise
