#
# Hellog World server in Python
# Binds REP socket to tcp:\\*:5555
# Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)    # Create REP (Reply) socket
socket.bind("tcp://*:5555") # Wait at port 5555

print("Server is running...")

while True:
    # Wait for next request from client
    message = socket.recv()
    print(f"Received requst: {message}")

    # Do some 'work'
    time.sleep(1)

    # Send reply back to client
    socket.send(b"World")