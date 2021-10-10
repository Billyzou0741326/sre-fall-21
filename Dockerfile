FROM node:16-alpine3.14 AS static_builder
COPY ./package*.json /app/
COPY ./*.config.js /app/
WORKDIR /app/
RUN npm install


FROM static_builder AS static
WORKDIR /app/
COPY ./css /app/css/
COPY ./templates /app/templates/
RUN npx postcss css/tailwind.css -o css/tailwind-output.css 


FROM python:3.8.12-alpine3.14 AS runtime
RUN apk add postgresql-libs &&                  \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev &&       \
        python3 -m pip install                  \
        Django==3.2.7                           \
        gunicorn==20.1.0                        \
        psycopg2-binary==2.9.1                  \
    &&                                          \
    apk --purge del .build-deps


FROM runtime
WORKDIR /app/
COPY . /app/
COPY --from=static /app/css/ /app/static/css/
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "-c", "python3 manage.py migrate && python3 manage.py collectstatic --no-input && gunicorn --bind 0.0.0.0:8000 sreproject.wsgi"]
