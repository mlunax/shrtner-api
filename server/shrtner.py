from flask import Flask, request

app = Flask("Shrtner")


@app.route("/api/v1")
def api():
    return "Hello Home!"


@app.route("/api/v1/put", methods=["POST"])
def put():
    a = request.json.get("data")
    return a


if __name__ == "__main__":
    app.run()