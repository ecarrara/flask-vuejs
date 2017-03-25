#!/bin/bash

cd /var/app

uwsgi --http :8080 \
    --chdir /var/app \
    --module application \
    --callable application \
    --master \
    --processes 1 \
    --threads 2 \
    --uid uwsgi \
    --gid uwsgi \
    --logto2 /var/log/uwsgi/uwsgi.log

