# Backend API
!MicroK8s Fullstack!
Source: https://www.codementor.io/@olawalealadeusi896/restful-api-with-python-flask-framework-and-postgres-db-part-1-kbrwbygx5

Credit to: Olawale Aladeusi

## Requirements
Python 3.8.5

## Setup
### Installation
1. Install Pip
```
$ pip3 install --upgrade pip
```
2. Install Pipenv
```
$ pip3 install pipenv
```
3. Install dependencies
```
$ pipenv install --dev
```
4. Run Flask app
```
$ pipenv shell
$ python run.py
```
5. Run with Gunicorn
```
$ gunicorn --bind 0.0.0.0:5000 run:app
```

### Database Migration
1. Create Postgres database using Docker
```
$ docker run --name postgres-docker -e POSTGRES_DB=postgresdb -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=password1 -p 5432:5432 -d postgres
```
2. Add Postgres database url to (.env) file
```
DATABASE_URL= postgres://admin:password1@localhost:5432/postgresdb
```
3. Create/update database tables
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
```
4. Verify database
```
$ docker exec -it postgres-docker bash
$ psql -d postgresdb -U admin
$ \dt
```
