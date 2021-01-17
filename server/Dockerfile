FROM python:slim AS build

COPY requirements.txt /requirements.txt
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt


FROM python:alpine

COPY --from=build /venv /venv
COPY . /app
WORKDIR /app
EXPOSE 5000

CMD [ "/venv/bin/python", "-u" ,"./shrtner.py" ]