# Django

## Normal Comands

```bash
$ # Starting
$ django-admin startproject mysite
$ python3 manage.py runserver 0.0.0.0:8000
$ python manage.py startapp polls

$ # Create super user
$ python manage.py create superuser

$ # Migrations
$ # tem que fazer migrations dos apps tambem.
$ python3 manage.py makemigrations #appname
$ python3 manage.py migrate
```

## Not too used

```bash
$ python3 manage.py sqlmigrate polls 0001 # Show migration.
$ python3 manage.py shell
$ python3 manage.py test polls
$ # -------
$ # Reset database, remove all migrations folders.
$ python3 manage.py flush
```

## Models comands

```bash
$ from django.contrib.auth.models import User
$ from social_media.models import Profile
$ # Filter by attr.
$ u1 = User.object.get(pk=1)
$ # Show all fields.
$ [o.name for o in Profile._meta.get_fields()]
```
