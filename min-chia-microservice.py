import zmq

#read clothing suggestions from the txt file
def read_clothing_suggestions():
    clothing_suggestions = {}
    with open("clothing_suggestions.txt", "r") as file:
        for line in file:
            weather, suggestion = line.strip().split(":")
            clothing_suggestions[weather.strip()] = suggestion.strip()
    return clothing_suggestions

#run microservice
def main():
    #set up sockets
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:4321")

    clothing_suggestions = read_clothing_suggestions()

    while True:
        #recieve the weather data from the client app
        weather_type = socket.recv_string()

        #look up clothing suggestions based on weather type from txt file
        if weather_type.lower() in clothing_suggestions:
            suggestion = clothing_suggestions[weather_type.lower()]
        else:
            suggestion = "Sorry, we don't have clothing suggestions for that weather."

        #send the clothing suggestions back
        socket.send_string(suggestion)

main()
