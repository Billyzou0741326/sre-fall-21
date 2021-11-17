FROM zguanhan/sre-f21-base:latest
WORKDIR /app/
COPY . /app/
EXPOSE 8000
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "--threads", "8", "sreproject.wsgi"]
