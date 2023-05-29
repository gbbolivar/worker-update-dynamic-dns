#!/bin/bash

UID=$(shell id -u)
WORKER_BA=python-worker-update-dynamic-dns


help: ## Show this help message
	@echo 'usage: make [target]'
	@echo
	@echo 'targets:'
	@egrep '^(.+)\:\ ##\ (.+)' ${MAKEFILE_LIST} | column -t -c 2 -s ':#'

start: ## Start the containers
	@U_ID=${UID} docker-compose up -d

stop: ## Stop the containers
	@U_ID=${UID} docker-compose stop

down: ## Stop the containers
	@U_ID=${UID} docker-compose down

restart: ## Restart the containers
	$(MAKE) stop && $(MAKE) start

build: ## Rebuilds all the containers
	@U_ID=${UID} docker-compose build

logs-f: ## bash into the backend container
	@U_ID=${UID} docker-compose logs -f

ssh-ba: ## bash into the backend container
	@U_ID=${UID} docker exec -it --user ${UID} ${WORKER_BA} /bin/sh
