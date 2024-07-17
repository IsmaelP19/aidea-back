FROM python:3.12.4-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y postgresql-client

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY wait-for-postgresql.sh /usr/local/bin/wait-for-postgresql.sh
RUN chmod +x /usr/local/bin/wait-for-postgresql.sh

COPY . .