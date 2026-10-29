

# Prefilled Assistant Messages
# Stop sequences 

# direct claude output in particular fashion 

def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {
            "temperature": temperature,
            "stopSequences":stop_sequences,
        },
    }

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]

# prefilled messages 

messages = []

add_user_message(messages, "Is coffee or tea better for breakfast")
add_assistant_message(messages,"Tea is better because ")

chat(messages)

# Stop Sequences
messages = []

add_user_message(messages, "Count from 1 to 100")
add_assistant_message(messages, stop_sequences=["5"])
add_assistant_message(messages, stop_sequences=["5", "3,4"]) # stop any one of them seen


chat(messages)