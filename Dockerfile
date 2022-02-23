FROM python:3.10.2-alpine
 
ENV PYTHONUNBUFFERED 1
RUN apk add --update --no-cache postgresql-client jpeg-dev
Shell
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

COPY ./requirements/dev.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps
RUN mkdir /messenger
COPY ./messenger /messenger
WORKDIR /messenger