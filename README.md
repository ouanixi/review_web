# Manual

This document guides the user to install the project in their local environment and demonstrates the functionality of the application

## Dependencies
- [Docker](https://www.docker.com/)

## Installation

Please make sure Docker is installed in your machine. Once you've installed the version adequate to your operating system, the rest of steps apply to any environment.

Docker installation details can be found [**here**][docker-installation]

[docker-installation]: https://docs.docker.com/engine/installation/

Once docker is installed, navigate to the root folder of both projects (`review_miner` and `review_web`) and run the following commands on each one of them (You will need two running terminals to execute them):

```sh
# build the containers
docker-compose build
```

```sh
# run the containers
docker-compose up
```


## Usage
Assuming the containers are both running, navigate to your localhost with port 8070 to view the application.

Type or copy and paste a user review in the given text box and hit submit.

![ ](/home/ouanixi/Work/Github/review_web/Screenshot from 2017-04-29 14-39-51.png  "review textbox")

The app should direct you to a new view where the summary of the review is displayed.

![ ](/home/ouanixi/Work/Github/review_web/Screenshot from 2017-04-29 14-39-24.png  "review summary")