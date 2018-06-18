# roxy-the-renovator

Django app for Roxy the Renovator
https://roxy-the-renovator.herokuapp.com/

Development
-----------

Fork the project on github and git clone your fork, e.g.:

    git clone https://bitbucket.com/<username>/roxy-the-renovator.git

Create a virtualenv using Python 3 and install dependencies. I recommend getting python3 via [homebrew](http://brew.sh/), then installing [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation) to that python. NOTE! You must change 'path/to/python3'
to be the actual path to python3 on your system.

    mkvirtualenv roxy-the-renovator --python=/path/to/python3
    pip install -r requirements.txt
    
Ensure node is installed. This can be done via homebrew:

    brew install node
    
Install javascript dependencies:

    npm install

Set environment variables as needed (check settings.py for values), e.g.

    export DATABASE_URL=postgres://username:password@127.0.0.1:5432/roxy-the-renovator
    export DJANGO_DEBUG=1

Set up db:

    createdb roxy-the-renovator
    python manage.py migrate

Run tests and view coverage:

    coverage run manage.py test
    coverage report -m

Check code style:

    flake8 .
    
Generate graph of data models, e.g.:

    python manage.py graph_models --pygraphviz -a -g -o all_models.png

Run server:

    python manage.py runserver

Lint JavaScript:

    jshint */static/*/js
    
    
Continuous Integration
----------------------
    
    This project is set up for CI using circle.
    
    Your build needs the following environment variables:
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    COVERALLS_REPO_TOKEN
    
    
Deployment
----------

This project is already set up for deployment to Heroku.

Make a new Heroku app, and add the following addons:
    
    heroku addons:create heroku-postgresql
    heroku addons:create mailgun
    heroku addons:create newrelic
    heroku addons:create papertrail
    
Set the Heroku config vars:

    ADMIN_EMAIL
    ADMIN_NAME
    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    DJANGO_SECRET_KEY
    DJANGO_SETTINGS_MODULE

Add Heroku buildpacks:

    heroku buildpacks:set heroku/nodejs -i 1
    heroku buildpacks:set heroku/python -i 2
