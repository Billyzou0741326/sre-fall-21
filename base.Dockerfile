FROM python:3.8.12-alpine3.14
RUN apk add postgresql-libs &&                  \
    apk add --virtual .build-deps gcc musl-dev  \
        postgresql-dev &&                       \
    python3 -m pip install                      \
        Django==3.2.7                           \
        gunicorn==20.1.0                        \
        psycopg2-binary==2.9.1                  \
    &&                                          \
    apk --purge del .build-deps
