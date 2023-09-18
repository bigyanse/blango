# blango
A blog application based on Django.

## Installation and Usage

This is for installing and using in development. If you want to deploy it, see [production](#production).

- `git clone https://github.com/bigyanse/blango.git`
- `cd blango`

If you use `pipenv`,

- `pipenv install`
- `pipenv shell`
- `python manage.py runserver`

If you prefer, python's `venv`,

- `python -m venv .env`
- `source .env/bin/activate.fish` or choose one that fits your shell environment.
- `python -m pip install -r requirements.txt`
- `python manage.py runserver`

## Production

In case, if you want to deploy this blog application to production by tweaking this project, here is how you can go about it.

- Make sure you have proper virtual environment setup for python.
- After that, you can install all the required packages using `python -m pip install -r requirements.txt`.
- The `db.sqlite3` database is only here for demo purpose. So, you may need to [setup](https://docs.djangoproject.com/en/4.2/intro/tutorial02/#database-setup) your own database. If you want to use sqlite as a database then you can just delete `db.sqlite3` named file in the directory and proceed the steps below. Else, configure the database you want and also, follow the steps below.
- Run `python manage.py migrate`.
- Set `DEBUG = False` in `core/settings.py`.
- Set `ALLOWED_HOSTS = ["*"]` in `core/settings.py` or your desired value.
- `python manage.py collectstatic`
- Now you can deploy it using `gunicorn core.wsgi`.
