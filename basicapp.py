import openai
from dotenv import load_dotenv
load_dotenv()
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex concepts with creative flair in simple language."},
    {"role": "user", "content": "Compose a poem that explains the concept of rebirth."}
  ],
  max_tokens=25,
  temperature=0.8,
  n=2
 )
print(completion.choices[0].message.content)
