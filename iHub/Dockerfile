FROM python:3

WORKDIR /project

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "manage.py", "runserver","127.0.0.1:8000"]