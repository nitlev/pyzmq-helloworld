#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
from datetime import datetime
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.0.17:5555")

#  Do 10 requests, waiting each time for a response
requests = []
for request in requests:
    print("Sending request …")
    socket.send_json()

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
