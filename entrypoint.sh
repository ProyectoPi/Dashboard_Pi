#!/usr/bin/env sh
set -e
flask db upgrade
exec gunicorn -k gthread --threads 4 -w 1 -b 0.0.0.0:8000 --access-logfile - run:app
