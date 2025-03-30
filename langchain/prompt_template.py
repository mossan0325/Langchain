from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
"""
以下の料理のレシピを教えてください。
{dish}
"""
)
prompt_value = prompt.invoke({"dish": "うどん"})
print(prompt_value.text)