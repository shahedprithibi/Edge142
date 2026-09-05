def detect_intent(message):
    if "hello" in message or "hey" in message: 
        return "greeting"

    elif "bye" in message or "goodbye" in message:
        return "farewell"

    else:
        return "unknown"


def respond(message):

    intent = detect_intent(message)

    if intent == "greeting":
        return "Hello, Prithibi. How may I help you?"

    elif intent == "farewell":
        return "Bye, Sir. Have a good day."

    else:
        return "I am not sure if I understand that yet"


while True:
    message = input()
    message = message.lower().strip()
    response = respond(message)
    print(response)
