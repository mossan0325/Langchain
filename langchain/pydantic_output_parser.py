from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field


class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredients of the dish")
    steps: list[str] = Field(description="steps to make the dish")

from langchain_core.output_parsers import PydanticOutputParser

output_parser = PydanticOutputParser(pydantic_object=Recipe)

format_instructions = output_parser.get_format_instructions()
print(format_instructions)

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "ユーザーが入力した料理のレシピを考えてください。\n\n"
            "{format_instructions}",
        ),
        ("human", "{dish}"),
    ]
)

prompt_with_format_instructions = prompt.partial(
    format_instructions=format_instructions
)

prompt_value = prompt_with_format_instructions.invoke({"dish": "カレー"})
print("=== role: system ===")
print(prompt_value.messages[0].content)
print("=== role: user ===")
print(prompt_value.messages[1].content)

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

ai_message = model.invoke(prompt_value)
print(ai_message.content)

recipe = output_parser.invoke(ai_message)
print(type(recipe))
print(recipe)