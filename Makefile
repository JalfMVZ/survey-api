test:
ifdef ComSpec
	set PYTHONPATH=. && pytest --maxfail=1 --disable-warnings -v
else
	PYTHONPATH=. pytest --maxfail=1 --disable-warnings -v
endif
up:
	docker-compose up --build

down:
	docker-compose down

migrate:
	docker-compose exec api alembic upgrade head

revision:
	docker-compose exec api alembic revision --autogenerate -m "$(name)"
