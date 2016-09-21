# MCIS-Bathroom-Status

This application is designed to ease the pain of walking to the bathroom only to find out all of the stalls are full. We have come up with an idea to create a website that will allow you to view the current status of the bathroom stalls via a sensor on the door. These sensors are connected to a Raspberry Pi (micro-computer), which hosts the website you are able to see to check the bathroom status.

# Setup

## Install dependencies

Python 3 is required.

We recommend using virtual environments for python projects. If python-virtualenv isn't installed, install it with `sudo apt-get install python-virtualenv` on Ubuntu.

## Setup virtual env

Issue command `virtualenv venv`

Activate virtual environment with `source venv/bin/activate`

## Run server

`python main.py`

## Seed data

If you need to have some data, run the seed_data.py script: `python seed_data.py`

