# genscape_test
Implementation of Genscape tech test

## Requirements
In order to get this running you have to install both docker and docker-compose. See documents if you don't have it installed now: https://docs.docker.com/compose/install/

After succesfull installation of docker, you have to execute script `build.sh`, which will build necessary docker images (if you are running on Windows you have to rename docker to docker.exe in build script):


```./build.sh```

Once images are built, you have to create `.env` file from teplate. Template contains default values for postgres, but it can contain other variables as well (in case of future developemnt and addition of extra servires):


```cp env_template .env```

## Starting of system

These are only required steps to get this tech demo working. To start you have to execute following command (if you are running on Windows you have to change docker-compose to docker-compose.exe):


```docker-compose up```

## Design of system

[System diagram](diagram.png)

