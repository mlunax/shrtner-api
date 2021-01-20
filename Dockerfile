FROM python:3.9-buster AS build

COPY requirements.txt /requirements.txt
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:alpine

RUN apk add --no-cache uwsgi-python3 tini
RUN apk version uwsgi-python3

COPY --from=build /venv /venv
COPY . /app

WORKDIR /app
EXPOSE 5000

ENV UWSGI_PLUGIN python3
ENV PYTHONPATH=$PYTHONPATH:/venv/lib/python3.9/site-packages

ENTRYPOINT ["/sbin/tini", "--"]
CMD [ "uwsgi", "--ini", "/app/shrtner.ini" ]