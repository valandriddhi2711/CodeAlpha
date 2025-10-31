import json
import random

# Load intents from file
with open("intents.json") as file:
    intents = json.load(file)

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Go through intents
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if user_input == pattern.lower():
                return random.choice(intent["responses"])

    return "I don't understand that. Try asking something else."

# Main loop
print("🤖 Chatbot is running! (enter 'bye' to exit chat)")
while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Chatbot: Goodbye! 👋")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)
