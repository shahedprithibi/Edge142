
def respond(message):

    if message == "hello buddy":
        return "Hello, Prithibi. how may I help you ?"

    elif message == "bye":
        return "Bye, Sir. Have a good day."

    else:
        return "I am not sure if i understand that yet"

while True:
    message = input()
    response = respond(message)
    print(response)
