import os
import openai
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/MtFuji_FujiCity.jpg/220px-MtFuji_FujiCity.jpg"

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "ユーザーが入力する画像に写っているものを答えてください。"},
        {
            "role": "user", 
            "content": [
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }
    ]
)

print(response.choices[0].message.content)