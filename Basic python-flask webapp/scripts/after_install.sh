#!/bin/bash

echo "Installing dependencies"

cd /home/ubuntu/flask-app

sudo apt-get update

sudo apt install -y python3-pip

sudo apt install -y python3-flask
