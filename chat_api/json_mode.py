import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "ユーザーの質問にJSON形式で回答してください。"},
        {"role": "user", "content": "こんにちは！森田です！"}
    ],
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)