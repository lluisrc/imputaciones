# Imputaciones RIU
This project is a time register app for automatize office go in and go out .

## Prerrequisites
Install docker (including docker-compose) on your environment.

## Startup
Clone the repository.
```
[user@linuxserver ~]$ git clone https://github.com/lluisrc/imputacionesriu.git
```
Go to clone directory and deploy the containers with docker-compose.
```
[user@linuxserver ~]$ cd imputacionesriu && docker-compose up -d
```
Go to your browser and visit the next url.
```
http://localhost:8000/register/registros/
```

## More about project
### Docker-compose
Docker-compose use imputacionesriu image from hub.docker.com --> https://hub.docker.com/r/lroca/imputacionesriu.<br>
Also docker-compose use a volume to get persistence for db<br>
<br>
Dockerfile.yml
```
version: '3'
services:
  app:
    image: lroca/imputacionesriu:v2
    ports:
      - 8000:8000
    volumes:
      - vol-imputacionesriu-1:/usr/src/app/db:rw
volumes:
  vol-imputacionesriu-1:
```
<img width="400" alt="Screenshot_15" style="text-align:center;" src="https://user-images.githubusercontent.com/60383607/184658830-d5c01586-82e4-41f8-8a81-ccce9e9b6847.png">

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
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
Once built the image I uploaded to Docker Hub.
Dockerfile
