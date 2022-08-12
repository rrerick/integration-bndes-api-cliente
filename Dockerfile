FROM python:3.9-buster

RUN mkdir /app
ENV APP_HOME /app
ENV PORT 8000
WORKDIR $APP_HOME

#python run in UNBUFFERED mode, the stdout and stderr streams are sent straight to terminal
ENV PYTHONUNBUFFERED 1

#install system requirements
RUN apt update -y

#install pip requirements
RUN python -m pip install --upgrade pip
RUN pip install -U pip setuptools==58.0

#install dependencies
COPY requirements*.txt ./
RUN pip install -r requirements.txt


# Run the web service on container startup.
# Here we use the python manage.py webserver,
CMD gunicorn --config gunicorn.conf.py connect_api.wsgi