# gifmarks #

A simple django app to bookmark funny gifs.
In categories.

## Running locally in a Virtual Environment ##

1. Clone this repository, activate a virtualenv, and `pip install -r
'requirements.txt'`
1. `gifmarks/settings.py` defaults to a postgres server on the local host; see
the file for connection information to set up your database and user.
1. Run `python manage.py syncdb` to create tables, and try to
`python manage.py runserver`. You may already be able to visit your app at
[http://127.0.0.1:8000](http://127.0.0.1:8000).
  a. The DB sync should prompt you to create an admin superuser. If not, create your
  admin superuser with `python manage.py createsuperuser` and enter
  some GIFs!


## Running on Heroku with Foreman and Gunicorn ##

1. There's a Procfile included in this repo, so try `foreman start` to make sure
it works. You may already be able to visit your app at [http://127.0.0.1:5000](http://127.0.0.1:5000)
  a. You may need to `gem install foreman` because that's how you get foreman.
1. Make sure you have the heroku toolbelt installed, and run your `heroku create`.
1. Once you set $DATABASE_URL, the local postgres config in settings.py will be
overridden, so don't worry about it.
1. Deploy your app to Heroku with `git push heroku master`, then `heroku run
python manage.py syncdb` and the application should load on your
`*.herokuapp.com` subdomain.
