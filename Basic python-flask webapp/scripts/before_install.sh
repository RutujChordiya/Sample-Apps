#!/bin/bash

echo "Stopping existing Flask application"
pkill -f "flask run" || true
