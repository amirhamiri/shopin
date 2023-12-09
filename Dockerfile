FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD gunicorn shopin.wsgi:application --bind 0.0.0.0:3000

ENV DJANGO_ENV=production

EXPOSE 3000
