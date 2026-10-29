
def chat(messages, system=None, temperature=1.0):
    # system_prompt="""
    # You are an AWS cloud support specialist. Your job is to answer user queries 
    # related to cloud hosting services on AWS.
    # """
    params = {
        "modelId": model_id, 
        "messages":messages,
        "inferenceConfig":{"temperature": temperature}
    }

    if system:
        params["system"] = [{"text": system}]

    response = client.converse(**params)

    return response["output"]["message"]["content"][0]["text"]

messages = []