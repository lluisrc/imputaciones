# Imputaciones RIU
This project is a time register app for automatize office go in and go out .

## Prerrequisites
Install docker on your environment.

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

- When you deploy a docker-compose, the containter have a volumen to read and write the db folder. Now the app have persistent data.
- In extras you can see the code of app and how i created the image.
