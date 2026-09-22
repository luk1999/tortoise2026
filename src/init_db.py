import asyncio
from datetime import date

from config import TORTOISE_ORM
from enums import Genre, UserStatus
from models import Author, Book, User
from services.users import UserService
from tortoise import Tortoise


async def init_data() -> None:
    clarke = await Author.create(first_name="Arthur Charles", last_name="Clarke", date_of_birth=date(1917, 12, 16))
    king = await Author.create(first_name="Stephen", last_name="King", date_of_birth=date(1947, 9, 21))
    grisham = await Author.create(first_name="John", last_name="Grisham", date_of_birth=date(1955, 2, 8))

    await Book.create(author=clarke, title="2001: A Space Odyssey", year=1968, genre=Genre.sci_fi)
    await Book.create(author=king, title="It", year=1986, genre=Genre.horror)
    await Book.create(author=king, title="The Shining", year=1977, genre=Genre.horror)
    gunslinger = await Book.create(author=king, title="The Gunslinger", year=1982, genre=Genre.fantasy)
    pelican = await Book.create(author=grisham, title="The Pelican Brief", year=1992, genre=Genre.thriller)
    rainmaker = await Book.create(author=grisham, title="The Rainmaker", year=1995, genre=Genre.thriller)

    smith = await User.create(
        username="john_smith",
        password=UserService.encode_password("12345678"),
        first_name="John",
        last_name="Smith",
        status=UserStatus.ACTIVE,
    )
    await smith.books.add(rainmaker, gunslinger)
    rambo = await User.create(
        username="rambo",
        password=UserService.encode_password("abcdefgh"),
        status=UserStatus.ACTIVE,
    )
    await rambo.books.add(pelican)
    await User.create(
        username="test_account",
        password=UserService.encode_password("abcd1234"),
        first_name="Test",
        last_name="Account",
        status=UserStatus.INACTIVE,
    )


async def main() -> None:
    print("Initializing db data...")
    try:
        await Tortoise.init(config=TORTOISE_ORM)
        await init_data()
    finally:
        await Tortoise.close_connections()
    print("Done.")


if __name__ == "__main__":
    asyncio.run(main())
