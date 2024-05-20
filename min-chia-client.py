import zmq

# main
def main():
    #set of socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:4321")  # Connecting to the microservice on same port

    # Weather data input
    weather_type = input("Please enter weather type (hot, cold, or rainy): ")

    # Send weather data to the microservice
    socket.send_string(weather_type)

    # Receive clothing suggestion from the microservice
    suggestion = socket.recv_string()
    print("Clothing suggestion:", suggestion)

main()
