FROM python:3.8
RUN apt-get update && \
    apt-get install -y gettext && \
    apt-get clean && rm -rf /var/cache/apt/* && rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
ENV PYTHONUNBUFFERED 1

RUN mkdir /src
WORKDIR /src

COPY Pipfile /src/
COPY Pipfile.lock /src/
RUN pip install pipenv
RUN pipenv install --system

