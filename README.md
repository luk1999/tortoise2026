# Tortoise2026

This project uses Python 3.13, Pipenv, Tortoise ORM, and Tortoise's native migration system.

## Create a virtual environment

From the project root, create the Pipenv virtual environment with Python 3.13:

```bash
python3.13 -m pip install --user pipenv
pipenv --python 3.13
```

Activate the virtual environment:

```bash
pipenv shell
```

Install the project and development dependencies:

```bash
pipenv install --dev
```

## Create the SQLite database and migrations

The SQLite database file is created automatically when Tortoise initializes the connection.

Initialize the migration package, create the initial migration, and apply it:

```bash
PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM init
PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM makemigrations -n initial
PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM migrate
```

This creates the local `db.sqlite3` file in the project root.

Use the Makefile shortcut for a fresh database:

```bash
make init-db-tortoise
```

## Initialize demo data

After creating the database and applying migrations, run the following from the project root
with the Pipenv virtual environment activated (`pipenv shell`):

```bash
make init-db-data
```

## Run the API

After installing dependencies and applying the database migrations, start the FastAPI server from the project root:

```bash
make run
```

The API is available at `http://127.0.0.1:8000`.
Interactive documentation is at `http://127.0.0.1:8000/docs` - you can use it for testing API calls.

## Development

### Database migrations

#### Generate auto migration

Use when you've changed something directly in models definitions.

```bash
make makemigrations
```

#### Generate custom migration

Use when you need to change something that is not reflected in model structure, like:
* data transformation
* initializing some models with data (eg. dict-like models)

```bash
PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM makemigrations --empty -n <name>
```

#### Apply migrations

```bash
make migrate
```

### Check code quality

Apply Ruff's automatic lint fixes to the source code:

```bash
make fix
```

Format the source code with Ruff:

```bash
make format
```
