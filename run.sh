#!/bin/bash

if [ $# -eq 0 ]; then
  poetry run python manage.py runserver
fi