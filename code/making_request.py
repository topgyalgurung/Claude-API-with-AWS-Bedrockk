import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")
model_id = "us.anthropic.claude-sonnet-4-20250514-v1:0"
user_message = {
    "role": "user",
    "content":[
        {"text": "whats 1+1?"}
    ]
}

response = client.converse(
    modelId=model_id,
    messages=[user_message]
)

response["output"]["message"]["content"][0]["text"]
# '1+1 = 2'


response["output"]["message"]
# "role": "user", "content":[{"text": "whats 1+1 = 2"}]