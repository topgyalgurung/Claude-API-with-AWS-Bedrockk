

messages = []

add_user_message(messages, "Write a 1 sentence description of a fake database")

response = client.converse_stream(messages=messages, modelId=model_id)

text = ""
for event in response["stream"]:
    if "contentBlockDelta" in event:
        chunk = event["contentBlockDelta"]["delta"]["text"]
        print(chunk, end="")
        text+= chunk
print("\n\nTotal Message:\n" + text)