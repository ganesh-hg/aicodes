import random

# Dictionary of possible user greetings and bot responses
greetings = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! How can I help you?",
    "hey": "Hey! How can I assist you?",
    "greetings": "Greetings! How can I assist you today?"
}

# Dictionary of possible user queries and bot responses
queries = {
    "product availability": "Please provide the name or description of the product you are looking for.",
    "order status": "To check your order status, please provide your order number.",
    "delivery information": "To get information about delivery, please provide your order number.",
    "payment options": "We accept various payment options including credit card, debit card, net banking, and UPI.",
    "store location": "We have multiple stores across the city. Please provide your location to find the nearest store."
}

def get_response(user_input):
    user_input = user_input.lower()
    response = ""

    # Check for greetings
    for greeting in greetings:
        if greeting in user_input:
            response = greetings[greeting]
            break

    # Check for queries
    for query in queries:
        if query in user_input:
            response = queries[query]
            break

    # If no specific response, provide a generic response
    if not response:
        response = "I'm sorry, but I couldn't understand your request. How can I assist you?"

    return response

# Example usage
print("JioMart ChatBot:")
print("---------------")
print("Bot: Hello! How can I assist you today?")

while True:
    user_input = input("User: ")
    bot_response = get_response(user_input)
    print("Bot:", bot_response)