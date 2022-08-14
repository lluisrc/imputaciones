# Imputaciones RIU
The imputaciones RIU project is a project to register times on my work.

## Prerrequisites
Install docker on your environment.

## Setup
1. First you should download the project on your workspace folder.
````
[user@linuxserver ~]$ git clone https://github.com/lluisrc/imputacionesriu.git
````
2. Now you can deploy a container
````
[user@linuxserver ~]$ docker-compose up -d
````
3. Go to your browser and visit the next url
````
http://localhost:8000/register/registros/
````

## How do it is structured
- When you deploy a docker-compose, the containter have a volumen to read and write the db folder. Now the app have persistent data.
- In extras you can see the code of app and how i created the image
