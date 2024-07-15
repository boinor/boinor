DOCKER_BASE_IMAGE := "boinor:dev"
DOCKER_CONTAINER_NAME := "boinor-dev"


image: Dockerfile pyproject.toml
	docker build \
	  -t boinor:dev \
	  .

docker:
	docker run \
	  -it \
	  --rm \
	  --name ${DOCKER_CONTAINER_NAME} \
	  --volume $(shell pwd):/code \
	  --user $(shell id -u):$(shell id -g) \
	  ${DOCKER_BASE_IMAGE} \
          bash

.PHONY: docker image
