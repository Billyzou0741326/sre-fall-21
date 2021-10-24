FROM zguanhan/sre-f21-base:latest
WORKDIR /app/
COPY . /app/
EXPOSE 8000
ENTRYPOINT ["/bin/sh", "-c", "python3 manage.py migrate && gunicorn --bind 0.0.0.0:8000 sreproject.wsgi"]
