#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
from sklearn.datasets import load_iris
import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://192.168.0.17:5555")

#  Do 10 requests, waiting each time for a response
datasets = load_iris()
data = datasets['data']

for row in data:
    print("Sending request …")
    socket.send_json(row.tolist())

    #  Get the reply.
    message = socket.recv()
    print("Received reply : %s" % message)
