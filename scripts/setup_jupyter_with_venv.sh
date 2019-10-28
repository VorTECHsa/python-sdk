#!/bin/bash

set -e

pip install ipykernel
python -m ipykernel install --name=${PWD##*/}