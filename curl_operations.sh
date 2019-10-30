#!/bin/bash

curl -X POST http://127.0.0.1:8000/wirecard/buyer -H 'content-type: application/json' -d '{"name": "adaao", "email": "armascarelli@gmail.com", "cpf": "11111111111"}'
