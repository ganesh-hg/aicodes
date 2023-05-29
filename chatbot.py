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
    
    
    ''' The code defines two dictionaries: greetings and queries. The greetings dictionary maps possible user greetings (keys) to corresponding bot responses (values). Similarly, the queries dictionary maps possible user queries (keys) to bot responses (values). These dictionaries provide the chatbot with predefined responses for different types of user inputs.

The get_response function takes a user input as a parameter and returns a bot response based on the input. It performs the following steps:

Converts the user input to lowercase using user_input.lower() to make it case-insensitive.
Initializes an empty string response to store the bot's response.
It then checks if the user input matches any of the greetings by iterating over the keys of the greetings dictionary. If a greeting is found in the user input, the corresponding response is assigned to the response variable.
Next, it checks if the user input matches any of the queries by iterating over the keys of the queries dictionary. If a query is found in the user input, the corresponding response is assigned to the response variable.
If no specific response is found, it assigns a generic response indicating that the input could not be understood.
Finally, it returns the response.

The code includes an example usage loop that simulates a conversation with the chatbot:

It starts by printing a greeting from the bot.
Inside the while loop, it prompts the user for input using input("User: ").
The user's input is then passed to the get_response function to obtain the bot's response.
The bot's response is printed using print("Bot:", bot_response).
The loop continues to prompt for user input and generate bot responses until it is interrupted or terminated.

Overall, the code provides a basic structure for a chatbot that can understand and respond to user inputs based on predefined greetings and queries. It can be expanded and customized by adding more greetings, queries, and corresponding responses to make the chatbot more interactive and useful.  '''
