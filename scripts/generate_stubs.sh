#!/usr/bin/env bash

#CURL --silent --header "Content-Type: application/json" -X POST \
#    --data '{"size":2}' "https://api.vortexa.com/v5/reference/charterers?apikey=${VORTEXA_API_KEY}" | jq ".data" \
#    > ../tests/api/examples/corporations.json
#
#CURL --silent --header "Content-Type: application/json" -X POST \
#    --data '{"size":2}' "https://api.vortexa.com/v5/reference/vessels?apikey=${VORTEXA_API_KEY}" | jq ".data" \
#    > ../tests/api/examples/vessels.json
#
#CURL --silent --header "Content-Type: application/json" -X POST \
#    --data '{"size":2}' "https://api.vortexa.com/v5/reference/products?apikey=${VORTEXA_API_KEY}" | jq ".data" \
#    > ../tests/api/examples/products.json
