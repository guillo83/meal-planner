[![Python application test with Github Actions](https://github.com/guillo83/meal-planner/actions/workflows/devops.yml/badge.svg)](https://github.com/guillo83/meal-planner/actions/workflows/devops.yml)

# Recipe parser
Sevice that parses a recipe and extracts important information such as the list of ingredients.

# How to run
To run this http service you can use these commands

Produce a new docker image:
make build

List all docker images:
docker images

From the listed images, select the IMAGE_ID of the repository called `deploy-fastapi`

docker run -p 127.0.0.1:8080:8080 <the IMAGE_ID>

