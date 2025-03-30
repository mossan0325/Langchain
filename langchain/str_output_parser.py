from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

ai_message = AIMessage(content="こんにちは。私はAIアシスタントです。")
ai_message = output_parser.invoke(ai_message)
print(type(ai_message))
print(ai_message)