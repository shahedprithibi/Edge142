import string

table = str.maketrans("", "", string.punctuation)


def normalize_input(message):
    message = message.lower().strip()
    message = message.translate(table)
    return message


def detect_intent(message):
    words = message.split()

    if "hello" in words or "hey" in words:
        return "greeting"

    elif "bye" in words or "goodbye" in words:
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
    message = normalize_input(message)
    response = respond(message)
    print(response)
