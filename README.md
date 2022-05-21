# Epic Events CRM

## Installation

### Prerequisites

- `python >= 3.9`, `pip`, `venv`
- If `python < 3.9`, you can manage different versions with **[pyenv](https://github.com/pyenv/pyenv)**
- `docker`, `docker-compose` for postgresSQL database

### Get started

#### Create virtual environment and install dependencies

```bash
$ python -m venv env
```

```bash
$ source env/bin/activate
```

```bash
$  pip install -r requirements.txt
```

#### Setting up postgreSQL database with the commands in `Makefile`

- Run docker containers. Equivalent to `docker-compose up -d`

```bash
$ make up
```

- Migrate database

```bash
$ python manage.py migrate
```

#### Create a superuser

```bash
$ python manage.py createsuperuser
```

> You can access admin dashboard on http://localhost:8000/admin

#### Or provide initial data from `fixtures/` directory

```bash
$ make fixture
```

## Running the app

```bash
$ python manage.py runserver
```

> The API is running on http://localhost:8000/ by default

## Documentation

Postman: https://documenter.getpostman.com/view/19947149/UyxoiPXf

## Author

- Jonny Saykosy <josayko@pm.me>

## License & copyright

© Jonny Saykosy

Licensed under the [MIT License](LICENSE).
