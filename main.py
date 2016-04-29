import zmq
import pandas as pd
from model import Model


def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    model = Model("model")

    while True:
        #  Wait for next request from client
        print("Waiting for message...")

        json = socket.recv_json()
        print("Received request: %s" % json)

        data = pd.read_json(json)

        #  Do some 'work'
        prediction = model.predict(data)

        #  Send reply back to client
        socket.send(b"%s" % prediction)


if __name__ == '__main__':
    main()
