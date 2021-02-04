# Backend API
!MicroK8s Fullstack!

## Requirements
Python 3.8.5

## Setup
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
$ pipenv install --system --deploy --skip-lock --ignore-pipfile
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
