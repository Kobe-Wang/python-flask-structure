# python-flask-structure
Python flask structure and directory convention specification

* Development

* How to run server?

```bash
  $ python manage.py runserver
```

* System dependencies

```bash
  $ pip3 install -r requirements.txt
  $ pip3 freeze > requirements/development.txt     # development package version
  $ pip3 freeze > requirements/staging.txt         # staging package version
  $ pip3 freeze > requirements/production.txt      # production package version
```

* Database init

```bash
  $ python3 manage.py db init
```

* Database migrate and upgrade

```bash
  $ python3 manage.py db migrate
  $ python3 manage.py db upgrade
```

* Deployment instructions

* How to run the test suite

```bash
  $ python3 manage.py test
```