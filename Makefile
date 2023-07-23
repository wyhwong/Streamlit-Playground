export DOCKER_BUILDKIT=1

export USERNAME?=$(shell whoami)
export USER_ID?=$(shell id -u)
export GROUP_ID?=$(shell id -g)
export TZ?=Asia/Hong_Kong

export DOCKER_NETWORK_NAME?=docker_network
export LOGLEVEL?=20
export HOST?=localhost
export VERSION?=devel

export BINANCE_API_KEY?=
export BINANCE_API_SECRET?=

network:
	docker network create ${DOCKER_NETWORK_NAME}

build:
	mkdir -p ./traefik
	docker-compose build

start:
	@echo "Running in ${MODE} mode"
	docker-compose -f docker-compose.yml -f docker-compose.labels.yml up -d --no-build

clean:
	docker-compose down --remove-orphans