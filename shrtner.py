from datetime import datetime

from flask import Flask, request, redirect

from repositories import RedirectRepository
from models import RedirectModel

app = Flask("Shrtner")


@app.route("/v1")
def api():
    return "Hello Shrtner!"


@app.route("/v1/put", methods=["POST"])
def put():
    data = request.json
    if RedirectRepository().get_url(data["key"]):
        return "This url key is exist in database", 409
    else:
        RedirectRepository().create(
            RedirectModel(
                url=data["url"],
                key=data["key"],
                timestamp=str(datetime.now().timestamp()),
            )
        )
    return data


@app.route("/v1/get/<string:key>", methods=["GET"])
def get(key: str):
    model = RedirectRepository().get_RedirectModel(key)
    if not model:
        return "This url key not found", 404
    else:
        return model.__dict__


@app.route("/v1/redirect/<string:key>", methods=["GET"])
def red(key: str):
    url = RedirectRepository().get_url(key)
    if not url:
        return "This url key not found", 404
    else:
        return redirect(url, code=302)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
