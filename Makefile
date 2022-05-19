all:	up

up:
	docker-compose -f database/docker-compose.yml up -d

fixture:
	python manage.py loaddata users clients contractStatus eventStatus contracts

psql:
	docker exec -it dev-postgres psql -U admin

down:
	docker-compose -f database/docker-compose.yml down

clean: down
	docker volume rm database_pgadmin-data
	docker volume rm database_postgres-data
