# Brief Overview
This microservice allows for the user to enter what kind of weather that are curretnly in or expecting to be in, and then see clothing suggestions based on what they entered.
This is completed through communication between the client script, the microservice script, and the .txt file, using ZeroMQ in python.

# Request Data
Requesting data is made easy with these scripts.

First, we want to make sure both the client.py application and microservice.py applications are running concurrently.
If they are, we will be asked to enter "hot", "cold", or "rainy." This input is what is sent to microservice to request data back.

We see in the client.py application, we are creating a connection to the same port as the microservie.py application, starting on line 6:

## context = zmq.Context()
## socket = context.socket(zmq.REQ)
## socket.connect("tcp://localhost:4321")

and on line 14, we send our weather data to the microservice, which is how we request data back:

## socket.send_string(weather_type)

# Recieve Data
The microservice then reads through the .txt file with the read_clothing_suggestions() function, stores the data, and sends it back to the 
client application in line 32:
## socket.send_string(suggestion)
