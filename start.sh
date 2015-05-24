#!/bin/bash
if [ $# -eq 0 ]; then
    echo "No argument detected. Please input the environment(dev/qa/prod)."
    exit 1
fi

if [ $1 = "dev" ]; then
    echo "Set environment to dev..."
    DJANGO_SETTINGS_MODULE="OmniTrader.settings"
    export DJANGO_SETTINGS_MODULE
    ./manage.py runserver
elif [ $1 = "qa" ]; then
    echo "Set environment to qa..."
    DJANGO_SETTINGS_MODULE="OmniTrader.settings_qa"
    export DJANGO_SETTINGS_MODULE
    ./manage.py runserver
elif [ $1 = "prod" ]; then
    echo "Set environment to prod..."
    DJANGO_SETTINGS_MODULE="OmniTrader.settings_prod"
    export DJANGO_SETTINGS_MODULE
    python3.4 manage.py runserver 0.0.0.0:8000
else
    echo "No such environment: $1"
    exit 1
fi

