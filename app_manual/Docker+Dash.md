# Using Docker for Dash Apps

## Why to use Docker?
Docker enables you to separate your applications from your infrastructure, allowing you to deliver software quickly. It helps you run your Dash application on other machines and clouds, ensuring that all the packages are installed and the app runs consistently.

Dockerizing your app may sound complex, but it's actually much easier than running it in other ways. This guide will walk you through the steps of running and developing a Dash app using Docker, providing examples along the way.

If you're not familiar with Docker concepts like docker images and containers, it's recommended to read about them before starting this guide. Additionally, this guide will explain more general methods for maintaining and using Docker Hub, which can be helpful for other purposes beyond Dash-Plotly apps.

## Dockerizing

### What Is Dockerizing?
Dockerizing is the process of packaging, deploying, and running applications using Docker containers.

### How to Dockerize a Dash App
By following the [project structure](Application_Structure.md) outlined in this guide, all files included under the 
`/app` directory will be part of the Docker image and run as a container.

### Why Use Gunicorn?
Gunicorn, short for "Green Unicorn," is a Python Web Server Gateway Interface (WSGI) HTTP server. It provides a 
production-grade server that ensures better performance, stability, and scalability for your Dash app. Gunicorn can 
handle concurrent requests, manage multiple worker processes, and provide other features that make it more suitable for 
production use.

### Why Does the Container Run on 0.0.0.0:8050?
When you use `0.0.0.0:8080`, the app inside the container will bind to all available network interfaces, including the 
host's network interface. This allows you to access the app using the host machine's IP address and the specified port, 
in this case, `8080`.

### Permissions and appUser
The user `appUser` is created as part of the Docker image and gets access to the directories it needs, 
such as logs and user input files. `appUser` is the default user that the app runs with inside the container.
It's important to note that the permissions you have when accessing the Docker container are very limited, 
mainly for monitoring and reading app logs. You can modify the Dockerfile to add more commands or permissions as needed.

### How to Dockerize Your App
To create a Docker image and run it as a container, use the following script:

```bash
/bin/bash ./scripts/dockerize_app.sh
```

---

## Using Dockerhub

#### Pushing images to Dockerhub
Dockerhub is the prefect please to share, save, and use docker-images.     
Customize the following script (mostly the changes you need to do are adding your user-name, password and the repo in 
your docker-hub account
```bash
/bin/bash ./scripts/push_image_to_dockerhub.sh
```

#### Consuming image from Dockerhub
Use this script for consuming the docker-image from dockerhub and run it locally.
```bash
/bin/bash ./scripts/run_app_from_dockerhub.sh
```

---

## Using and maintaining a docker base dash app 
#### Access the running container
To access the running container, use the following command:
```BASH
docker exec -it bpo_app /bin/bash
```


#### Cleanup Docker components 
Run this script to clean up old/unused Docker images, containers, and other Docker components on your machine. 
Make sure to backup everything before running it:
```bash
/bin/bash ./scripts/docker_hard_cleanup.sh
```

