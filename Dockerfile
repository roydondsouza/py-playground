FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev && \
    pip3 install --upgrade pip setuptools

# We copy this file first to leverage docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]