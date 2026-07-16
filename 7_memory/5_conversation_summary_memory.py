from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(temperature=0)

memory = ConversationSummaryMemory(llm=llm)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "my name is Alice"}, {"output": "nice to meet you Alice"})

# Will output a summary instead of raw messages
print(memory.load_memory_variables({}))
