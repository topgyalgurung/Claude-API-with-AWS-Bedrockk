from multiturn_message import add_assistant_message, add_user_message, chat

# Make an initial list of messages
messages = []

# Use a 'while True' loop to run the chatbot forever
while True:
    # Get user input
    user_input = input("> ")
    print(f"> {user_input}")

    # Add user's input to list of messages
    add_user_message(messages, user_input)

    # Send list of messages to the API
    text = chat(messages)

    # Add generated text to list of messages
    add_assistant_message(messages, text)
    
    # Print the generated text
    print(text)