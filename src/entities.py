from models import Author, Book, User
from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator

Tortoise.init_models(["models"], "models")

BaseBook = pydantic_model_creator(
    Book,
    name="BaseBook",
    include=("id", "title", "year", "genre"),
)

BaseAuthor = pydantic_model_creator(
    Author,
    name="BaseAuthor",
    include=("id", "first_name", "last_name", "date_of_birth"),
)

BaseAuthorWithBooks = pydantic_model_creator(
    Author,
    name="BaseAuthorWithBooks",
    include=("id", "first_name", "last_name", "date_of_birth", "books"),
    exclude=("books.author", "books.author_id", "books.users"),
)

BaseBookWithAuthor = pydantic_model_creator(
    Book,
    name="BaseBookWithAuthor",
    include=("id", "title", "year", "genre", "author"),
    exclude=("author.books",),
)

BaseUser = pydantic_model_creator(
    User,
    name="BaseUser",
    include=("id", "username", "first_name", "last_name", "status"),
)

BaseUserWithBooks = pydantic_model_creator(
    User,
    name="BaseUserWithBooks",
    include=("id", "username", "first_name", "last_name", "status", "books"),
    exclude=("books.author", "books.author_id", "books.users"),
)
