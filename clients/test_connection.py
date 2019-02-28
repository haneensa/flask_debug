"""
at the server side:

@app.route("test/connection", methods=["GET", "POST"])
def connect()
    return Response(json.dumps(["success"]))
"""
import logging, requests, timeit
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

url = "http://100.64.0.1:8000/test/connection"
#url = "http://0.0.0.0:8000/test/connection"

multi = timeit.timeit('_ = requests.get("%s")'%url, 'import requests', number=100)
onesession = timeit.timeit('_ = session.get("%s")'%url, 'import requests; session = requests.Session()', number=100)

print "multi sessions: %s ms, one session %s ms" % (multi * 10.0, onesession * 10.0)
