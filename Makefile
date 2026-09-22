.PHONY: requirements test init-db fix format run

requirements:
	pipenv requirements > requirements.txt
	pipenv requirements --dev > requirements_dev.txt

init-db-tortoise:
	PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM init
	PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM makemigrations -n initial
	PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM migrate

init-db-data:
	PYTHONPATH=src python src/init_db.py

makemigrations:
	PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM makemigrations

migrate:
	PYTHONPATH=src pipenv run tortoise -c config.TORTOISE_ORM migrate

run:
	PYTHONPATH=src pipenv run uvicorn main:app --app-dir src --reload

fix:
	pipenv run ruff check --fix src

format:
	pipenv run ruff format src
