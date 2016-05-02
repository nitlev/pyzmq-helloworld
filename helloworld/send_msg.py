from __future__ import print_function
from time import time
from datetime import timedelta
from sklearn.datasets import load_iris
import zmq


def get_socket():
    context = zmq.Context()

    #  Socket to talk to server
    print("Connecting to hello world server...")
    socket = context.socket(zmq.REQ)
    return socket


def send_message(socket, address):
    socket.connect(address)

    datasets = load_iris()
    data = datasets['data']

    start = time()
    number_of_rows_sent = 0

    for row in data:
        socket.send_json([row.tolist()])
        number_of_rows_sent += 1

        #  Get the reply.
        message = socket.recv()
        print("Received prediction : %s" % message)

    end = time()
    time_elapsed = timedelta(seconds=end - start)

    print("Got %s predictions in %s" % (number_of_rows_sent, time_elapsed))


def send():
    socket = get_socket()
    send_message(socket, "tcp://192.168.0.17:5555")


if __name__ == '__main__':
    send()
