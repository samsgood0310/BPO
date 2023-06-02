## Using Docker for running Dash App's

This guid assume that you know what is Docker-Image, Docker-Container, and have a basic knowledge of how to use them.


#### Creating a Docker-Image + running it as a Container
run the following command from the current location of this document.
```BASH
/bin/bash ../AppAdmin-Scripts/dockerize_app.sh
```
#### Access the running container
run
```BASH
docker exec -it bpo_app /bin/bash
```
All files will be under the app/ dir. 
then you will be using appUser.

* Notice: the permissions you have when accessing the docker container are very limited, and the main use case is for
monitoring and reading the app logs.
* Notice: you can change the dockerfile and add more commands that you need or add permissions.
