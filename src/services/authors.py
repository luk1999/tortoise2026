from entities import BaseAuthor, BaseAuthorWithBooks
from errors import DoesNotExistError
from models import Author
from tortoise.exceptions import DoesNotExist


class AuthorService:
    @staticmethod
    async def get_all() -> tuple[BaseAuthor]:
        authors = await Author.all()
        return tuple([await BaseAuthor.from_tortoise_orm(author) for author in authors])

    @staticmethod
    async def get(author_id: int) -> BaseAuthorWithBooks:
        try:
            author = await Author.filter(books__isnull=False).distinct().prefetch_related("books").get(id=author_id)
            return await BaseAuthorWithBooks.from_tortoise_orm(author)
        except DoesNotExist as error:
            raise DoesNotExistError from error
