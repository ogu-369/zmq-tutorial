#
# Hello World client in Python
# Connects REQ socket to tcp://localhost:5555
# Sends "Hello" to server, expects "World" back
#

import zmq


context = zmq.Context()

# Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)    # Create REQ (Request) socket
socket.connect("tcp://localhost:5555")  # Connect to server

# Do 10 requests, waiting each time for a response
for request in range(10):
    print(f"Sending request {request} ...")
    socket.send(b"Hello")

    # Get the reply
    recv_message = socket.recv()
    print(f"Received reply {request} [ {recv_message} ]")