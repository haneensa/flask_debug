# wsgi entry point

# import flask app and run it?
from server import app


if __name__ == "__main__":
    print "hi"
    app.run(debug=True, threaded=True)
