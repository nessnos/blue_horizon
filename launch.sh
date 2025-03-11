#!/bin/bash

poetry install

PORT=8000
PID=$(lsof -ti :$PORT)
if [ -n "$PID" ]; then
    kill -9 $PID
fi

CELERY_PID=$(pgrep -f "celery -A water worker --loglevel=info")
if [ -n "$CELERY_PID" ]; then
    kill -9 $CELERY_PID
fi

poetry run celery -A water worker --loglevel=info >> celery.log 2>&1 &
poetry run python manage.py runserver &

cd webapp
npm install
npm run dev
