FROM python:3.10.2-alpine

ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache postgresql-client jpeg-dev &&\
    apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev &&\
    apk del .tmp-build-deps &&\
    apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

WORKDIR /app

COPY requirements/ /requirements
RUN pip install -r /requirements/dev.txt

RUN apk del .tmp-build-deps
COPY . .
