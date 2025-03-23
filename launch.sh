#!/bin/bash
OS=$(uname)

echo "Starting poetry install..."
poetry install

PORT=8000
echo "Checking if port $PORT is in use..."
if [[ "$OS" == "Darwin" ]]; then  # macOS
    PIDS=$(lsof -t -i :$PORT)
else  # Linux
    PIDS=$(netstat -tulpn 2>/dev/null | grep ":$PORT" | awk '{print $7}' | cut -d/ -f1)
fi

if [[ -n "$PIDS" ]]; then
    echo "Killing processes on port $PORT: $PIDS"
    kill -9 $PIDS

    for PID in $PIDS; do
        while kill -0 "$PID" >/dev/null 2>&1; do
            echo "Waiting for process with PID $PID to terminate..."
            sleep 1
        done
    done

    echo "All processes using port $PORT have been terminated, port is now free."
else
    echo "No valid process found on port $PORT"
fi

echo "Checking for running Celery workers..."
CELERY_PIDS=$(pgrep -f "celery -A water worker --loglevel=info")

if [[ -n "$CELERY_PIDS" ]]; then
    echo "Killing Celery workers: $CELERY_PIDS"
    kill -9 $CELERY_PIDS

    for PID in $CELERY_PIDS; do
        while kill -0 "$PID" >/dev/null 2>&1; do
            echo "Waiting for Celery worker with PID $PID to terminate..."
            sleep 1
        done
    done

    echo "All Celery workers have been stopped."
else
    echo "No Celery worker found"
fi

echo "Starting Celery worker..."
poetry run celery -A water worker --loglevel=info >> celery.log 2>&1 &

echo "Starting Django development server..."
poetry run python manage.py runserver &

echo "Installing and running the webapp..."
cd webapp
npm install
npm run dev

