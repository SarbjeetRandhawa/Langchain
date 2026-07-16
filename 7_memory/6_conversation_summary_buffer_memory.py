from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0)

# Keeps exact messages up to 50 tokens, then summarizes older ones
memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=50)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "my name is Bob"}, {"output": "nice to meet you Bob"})

print(memory.load_memory_variables({}))
