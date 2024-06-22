#!/bin/bash

echo "Starting Flask application"
cd /home/ubuntu/flask-app
export FLASK_APP=main.py
nohup flask run --host=0.0.0.0 --port=80 &
