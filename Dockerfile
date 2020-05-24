FROM python:3.7.5

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN mkdir /config

ADD requirements /config
RUN pip install --upgrade pip
RUN pip install -r /config/requirements.txt

ADD src /code