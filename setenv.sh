#!/bin/bash
if [ $# -eq 0 ]; then
    echo "No argument detected. Please input the environment(dev/qa/prod)."
    exit 1
fi

if [ $1 = "dev" ]; then
    echo "Set environment to dev..."
    DJANGO_SETTINGS_MODULE="settings"
elif [ $1 = "qa" ]; then
    echo "Set environment to qa..."
    DJANGO_SETTINGS_MODULE="settings_qa"
elif [ $1 = "prod" ]; then
    echo "Set environment to prod..."
    DJANGO_SETTINGS_MODULE="settings_prod"
else
    echo "No such environment: $1"
    exit 1
fi
export DJANGO_SETTINGS_MODULE

