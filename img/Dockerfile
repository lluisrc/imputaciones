FROM python:3.9

WORKDIR /usr/src/app
RUN pip install django

COPY . .

EXPOSE 8000

CMD ["/bin/bash", "-c", "python manage.py migrate && python manage.py makemigrations && python manage.py runserver 0.0.0.0:8000"]
