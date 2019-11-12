#!/usr/bin/env bash
. venv/bin/activate
rm -rf dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD --repository-url https://test.pypi.org/legacy/ dist/*
