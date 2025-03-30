from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "user",
            [
                {"type": "text", "text": "画像を説明してください。"},
                {"type": "image_url", "image_url": {"url": "{image_url}"}},
            ],
        ),
    ]
)
image_url = "https://raw.githubusercontent.com/yoshidashingo/langchain-book/main/assets/cover.jpg"

prompt_value = prompt.invoke({"image_url": image_url})
print(prompt_value)

model = ChatOpenAI(model="gpt-4o", temperature=0)
ai_message = model.invoke(prompt_value)
print(ai_message.content)