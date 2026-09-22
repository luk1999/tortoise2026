from entities import BaseBook, BaseBookWithAuthor
from errors import DoesNotExistError
from models import Book
from tortoise.exceptions import DoesNotExist


class BookService:
    @staticmethod
    async def get_all() -> tuple[BaseBook]:
        books = await Book.all()
        return tuple([await BaseBook.from_tortoise_orm(book) for book in books])

    @staticmethod
    async def get(book_id: int) -> BaseBookWithAuthor:
        try:
            book = await Book.get(id=book_id).prefetch_related("author")
            return await BaseBookWithAuthor.from_tortoise_orm(book)
        except DoesNotExist as error:
            raise DoesNotExistError from error
