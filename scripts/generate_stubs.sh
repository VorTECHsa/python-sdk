#!/usr/bin/env bash


CURL --silent --header "Content-Type: application/json" -X POST \
    --data '{"size":2}' "https://api.vortexa.com/v5/reference/charterers?apikey=${VORTEXA_API_KEY}" | jq ".data" \
    > ../test/api/examples/charterers.json

CURL --silent --header "Content-Type: application/json" -X POST \
    --data '{"size":2}' "https://api.vortexa.com/v5/reference/vessels?apikey=${VORTEXA_API_KEY}" | jq ".data" \
    > ../test/api/examples/vessels.json