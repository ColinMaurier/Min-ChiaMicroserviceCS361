# Brief Overview
This microservice allows for the user to enter what kind of weather that are curretnly in or expecting to be in, and then see clothing suggestions based on what they entered.
This is completed through communication between the client script, the microservice script, and the .txt file, using ZeroMQ in python.

# Request Data
Requesting data is made easy with these scripts.
We see in the client.py application, we are creating a connection to the same port as the microservie.py application, starting on line 6:

## context = zmq.Context()
## socket = context.socket(zmq.REQ)
## socket.connect("tcp://localhost:4321")
