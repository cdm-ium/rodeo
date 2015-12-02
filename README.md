# rodeo

Picture Service


## Quickstart

First, set your app's secret key as an environment variable. For example, add the following to ``.bashrc`` or ``.bash_profile``:

    export RODEO_SECRET='something-really-secret'

Create a virtualenv for the project, using ``virtualenvwrapper``:

    mkvirtualenv rodeo

Then run the following commands to bootstrap your environment.

    git clone https://github.com/globality-corp/rodeo
    cd rodeo
    pip install -e .

You will also need to create the local PostgreSQL database initially:

    createdb rodeo_db


## Running locally

To run the server locally in debug mode:

1. Seed the database (whenever you wish to re-seed data):

    createall

1. Run the server (can specify custom port using -p <port>):

    python manage.py runserver -p9000

# Sample Requests

To create a new picture:

   http -j  POST http://127.0.0.1:5401/api/v1/picture author="james" file_id="sflkafguh" 

To retrieve an existing picture:

   http -j  GET http://127.0.0.1:5401/api/v1/picture/50ce76c2-ae37-40a1-9439-05709823e2a0

## Running Tests

To run all tests, run:

    python setup.py nosetests
