
# Using both prefilled message and stop sequence to get structured data oupt 

import json

messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
text

json.loads(text.strip())