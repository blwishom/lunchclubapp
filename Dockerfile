ARG PYTHON_VERSION=3.10-slim-buster

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /FlaskApp

COPY requirements1.txt /tmp/requirements.txt

WORKDIR /FlaskApp

RUN set -ex && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY ./FlaskApp .

EXPOSE 8000

# replace demo.wsgi with <project_name>.wsgi
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "demo.wsgi"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]
