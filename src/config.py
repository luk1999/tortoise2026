from typing import Any

TORTOISE_ORM: dict[str, Any] = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": ["models"],
            "default_connection": "default",
            "migrations": "models.migrations",
        }
    },
}
