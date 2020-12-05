Inspired from: https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

```
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate --noinput
```