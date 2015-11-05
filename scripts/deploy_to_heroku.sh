#!/bin/bash

# This script will quit on the first error that is encountered.
set -e

CIRCLE=$1
export DJANGO_DEBUG=0

DEPLOY_DATE=`date "+%FT%T%z"`
SECRET=$(openssl rand -base64 58 | tr '\n' '_')

heroku config:set --app=roxy-the-renovator \
NEW_RELIC_APP_NAME='roxy-the-renovator' \
ADMIN_EMAIL="jessamyn.smith@gmail.com" \
ADMIN_NAME="Roxy the Renovator" \
DJANGO_SETTINGS_MODULE=roxy_the_renovator.settings \
DJANGO_SECRET_KEY="$SECRET" \
DEPLOY_DATE="$DEPLOY_DATE" \
> /dev/null

python manage.py collectstatic --noinput -i node_modules -i themes -i less -i src
python manage.py compress

if [ $CIRCLE ]
then
    git fetch origin --unshallow
    git push git@heroku.com:roxy-the-renovator.git $CIRCLE_SHA1:refs/heads/master
else
    git push heroku master
fi

heroku run python manage.py migrate --noinput --app=roxy-the-renovator
