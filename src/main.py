from contextlib import asynccontextmanager
from http import HTTPStatus

from config import TORTOISE_ORM
from errors import ConflictError, DoesNotExistError, ForbiddenError
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routes import users
from services.authors import AuthorService
from services.books import BookService
from tortoise import Tortoise


@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(config=TORTOISE_ORM)
    try:
        yield
    finally:
        await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)


@app.exception_handler(DoesNotExistError)
async def does_not_exist_handler(request: Request, exc: DoesNotExistError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"detail": "Not Found"})


@app.exception_handler(ForbiddenError)
async def forbidden_handler(request: Request, exc: ForbiddenError):
    return JSONResponse(status_code=HTTPStatus.FORBIDDEN, content={"detail": str(exc)})


@app.exception_handler(ConflictError)
async def conflict_handler(request: Request, exc: ConflictError):
    return JSONResponse(status_code=HTTPStatus.CONFLICT, content={"detail": str(exc)})


@app.get("/")
async def root():
    return {"message": "Ready"}


@app.get("/authors")
async def get_authors():
    return await AuthorService.get_all()


@app.get("/authors/{author_id}")
async def get_author(author_id: int):
    return await AuthorService.get(author_id)


@app.get("/books")
async def get_books():
    return await BookService.get_all()


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    return await BookService.get(book_id)


app.include_router(users.router)
