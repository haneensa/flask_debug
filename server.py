from flask import Flask, Response, render_template, request
import json
def setup_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/test/connection", methods=["GET", "POST"])
    def conn():
        data = request.get_json()
        print "test/connection", data
        return Response(json.dumps(["success"]))

if __name__ == "__main__":
    app = Flask(__name__)
    
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"


    setup_routes(app)
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
