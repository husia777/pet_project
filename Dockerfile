

FROM python:3.11

WORKDIR /app 

COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python -m pip install python-dotenv
COPY . .
CMD [ "python", "../manage.py", "runserver", "0.0.0.0:8000"]


