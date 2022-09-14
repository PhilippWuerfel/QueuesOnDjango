FROM python:3.10-slim-buster

# set work directory
WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # install netcat
    && apt-get -y install netcat \
    # cleaning up unused files
    && apt-get clean \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# copy project requirements
COPY ./requirements.txt /requirements.txt

# Requirements are installed here to ensure they will be cached.
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# copy project
COPY . /usr/src/app/

# lint
# RUN pip install flake8==3.8.4 click==8.0.4 black==21.5b1
# RUN flake8 .
RUN pip install black
RUN black . --check --exclude=migrations

# copy entrypoints and make them executable 
COPY ./compose/local/django/start /start-django
RUN sed -i 's/\r$//g' /start-django
RUN chmod +x /start-django

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower