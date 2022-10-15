# Imputaciones
This project is a time register app for automatize office go in and go out .

## Pre requisites
Install docker (including docker-compose) on your environment.

## Startup
Clone the repository.
```
[user@linuxserver ~]$ git clone https://github.com/lluisrc/imputaciones.git
```
Go to clone directory and deploy the containers with docker-compose.
```
[user@linuxserver ~]$ cd imputaciones && docker-compose up -d
```
Go to your browser and visit the next url.
```
http://localhost:8000/register/registros/
```
<img width="912" alt="Screenshot_25" src="https://user-images.githubusercontent.com/60383607/195981828-2c4719cd-463e-45ec-92e6-86008b564920.png">
<img width="944" alt="Screenshot_24" src="https://user-images.githubusercontent.com/60383607/195981832-5f18bb18-6dc8-4e22-a3fc-f25a855ae538.png">

## More about project
### Docker-compose
Docker-compose use imputaciones image from hub.docker.com --> https://hub.docker.com/r/lroca/imputaciones.<br>
Also docker-compose use a volume to get persistence for db<br>
If you want to delete data of database you can delete the persistent volumen `docker volume rm imputaciones_vol-imputaciones-1`. Docker-compose will recreate other persistent volume<br>
<br>
Dockerfile.yml
```
version: '3'
services:
  app:
    image: test01:v2
    ports:
      - 8000:8000
    volumes:
      - vol-imputaciones-1:/usr/src/app/db:rw
volumes:
  vol-imputaciones-1:
```
<img width="400" alt="Screenshot_15" src="https://user-images.githubusercontent.com/60383607/184658830-d5c01586-82e4-41f8-8a81-ccce9e9b6847.png">

### Dockerfile
I have built the image from this Dockerfile<br>
<br>
Dockerfile
```
FROM python:3.9

WORKDIR /usr/src/app
RUN pip install django

COPY . .

EXPOSE 8000

CMD ["/bin/bash", "-c", "python manage.py migrate && python manage.py makemigrations && python manage.py runserver 0.0.0.0:8000"]
```
Once built the image I uploaded to Docker Hub.
Dockerfile
