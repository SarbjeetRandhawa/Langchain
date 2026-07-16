from langchain.memory import ConversationEntityMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0)

memory = ConversationEntityMemory(llm=llm)
# Extracts and stores facts about specific entities (e.g., 'Alice', 'Google')
_input = {"input": "Alice works at Google."}
memory.save_context(
    _input,
    {"output": "That's a great place to work."}
)

print(memory.load_memory_variables({"input": "Where does Alice work?"}))
