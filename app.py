import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OpenAI.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI()

# add your completion code
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]

# make completion
completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

# print response
print(completion.choices[0].message.content)