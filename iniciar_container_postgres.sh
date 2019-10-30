#!/bin/bash

systemctl stop postgresql

docker run --rm --name pg_docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v /home/adaao/dev/docker_volumes/postgres:/var/lib/postgresql/data  postgres

docker ps

sleep 2

psql -h localhost -U wirecard

