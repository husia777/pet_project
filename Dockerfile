FROM python:3.10-slim
RUN apt-get update -y
RUN apt-get upgrade -y
WORKDIR /usr/src/app
RUN apt-get update -y
RUN apt-get upgrade -y
COPY . .

RUN pip freeze > requirements.txt


CMD python ./manage.py runserver