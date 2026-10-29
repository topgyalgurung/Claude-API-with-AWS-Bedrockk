# System Message and Temperature 

def chat(messages, system=None):
    # system_prompt="""
    # You are an AWS cloud support specialist. Your job is to answer user queries 
    # related to cloud hosting services on AWS.
    # """
    params = {
        "modelId": model_id, 
        "messages":messages,
    }

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]

messages = []

add_user_message(messages, "How do I host a Postgres database?")
text = chat(messages, system="You are  an AWS Support specialist")

print(text)


