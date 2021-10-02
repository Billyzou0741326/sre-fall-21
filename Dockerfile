FROM python:3.8.12-alpine3.14 AS runtime
RUN apk add postgresql-libs &&      \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev &&   \
    python3 -m pip install          \
        Django==3.2.7               \
        gunicorn==20.1.0            \
        psycopg2-binary==2.9.1      \
    &&                              \
    apk --purge del .build-deps

FROM runtime
WORKDIR /app/
COPY . /app/
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "-c", "./manage.py collectstatic && ./manage.py runserver 0.0.0.0:8000"]
# ENTRYPOINT SECRET_KEY=${SECRET_KEY}     \
#     PG_USER=${PG_USER}                  \
#     PG_DATABASE=${PG_DATABASE}          \
#     EXTERNAL_IP=${EXTERNAL_IP}          \
#     python manage.py runserver 0.0.0.0:8000
