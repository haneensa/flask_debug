"""
at the server side:

@app.route("test/connection", methods=["GET", "POST"])
def connect()
    return Response(json.dumps(["success"]))
"""
import logging, requests, time
logging.basicConfig(level=logging.DEBUG, format="%(message)s")
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


timestep = lambda: int(round(time.time() * 1000))
url = "http://100.64.0.1:8000/test/connection"
#url = "http://0.0.0.0:8000/test/connection"
session = requests.Session()

request_time = timestep()
r = session.get(url)
answer_time = timestep()
print "round trip", answer_time - request_time
print(str(r.content))

request_time = timestep()
r = session.get(url)
answer_time = timestep()
print "round trip", answer_time - request_time
print(str(r.content))

request_time = timestep()
r = session.get(url)
answer_time = timestep()
print "round trip", answer_time - request_time


print(str(r.content))
