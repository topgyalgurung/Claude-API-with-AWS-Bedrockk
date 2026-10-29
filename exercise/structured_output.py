"""
- use message prefilling and stop sequences to get three different commands in single response
- there should not be any comments or explanation

"""

messages = []

prompt = """
Generate three different sample AWS CLI commands. Each should be very short.
"""

add_user_message(messages, prompt)
add_asssitant_message(messages, "Here are all three commands in a single block without any comments:\n```bash ")

text = chat(messages, stop_sequences=["```"])
text.strip()

