# Django

## Comands

```bash
$ # Starting
$ django-admin startproject mysite
$ python3 manage.py runserver 0.0.0.0:8000
$ python manage.py startapp polls

$ # Create super user
$ python manage.py create superuser

$ # Migrations
$ # tem que fazer migrations dos apps tambem.
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## Comands not too used

```bash
$ python3 manage.py sqlmigrate polls 0001 # Show migration.
$ python3 manage.py shell
```
