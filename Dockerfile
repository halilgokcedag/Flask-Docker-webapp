# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Working Directory
WORKDIR /app

# Copy the source code and requirements.txt file to the app directory
COPY app/requirements.txt /app/
COPY app/server-flask.py /app/

RUN useradd -m -u 3000 webapp && chown -R webapp:webapp /app
USER webapp

# Install packages from requirements.txt
RUN pip3 install -r /app/requirements.txt

EXPOSE 5000

CMD [ "python3", "/app/server-flask.py" ]
