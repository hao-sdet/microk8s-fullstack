FROM python:3.8-alpine

RUN apk add --update py3-pip && \ 
	apk add --virtual build-deps gcc python3-dev musl-dev && \
    	apk add postgresql-dev && \ 
	apk add libffi-dev && \ 
	apk add musl-dev && \ 
	apk add libgcc

RUN pip3 install --upgrade pip

RUN pip3 install pipenv

COPY . /usr/src/flask-rest-api-backend
WORKDIR /usr/src/flask-rest-api-backend

RUN pipenv install --system --deploy --skip-lock

EXPOSE 5000

CMD ["gunicorn", "--bind","0.0.0.0:5000", "run:app"]
