from flask import Flask, Response, render_template, request
import json

app = Flask(__name__)
from werkzeug.debug import DebuggedApplication
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)

app.debug = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test/connection", methods=["GET", "POST"])
def conn():
    data = request.get_json()
    print "test/connection", data
    return Response(json.dumps(["success"]))

from werkzeug.serving import WSGIRequestHandler
WSGIRequestHandler.protocol_version = "HTTP/1.1"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False, threaded=True)
