from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

llm = ChatOpenAI(temperature=0)
chain = prompt | llm

# Simple dictionary to store session histories
store = {}
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Wrap the chain with history functionality
with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# First interaction
res1 = with_message_history.invoke(
    {"input": "Hi, I'm Bob!"},
    config={"configurable": {"session_id": "user_1"}}
)
print("Turn 1:", res1.content)

# Second interaction (remembers name)
res2 = with_message_history.invoke(
    {"input": "What's my name?"},
    config={"configurable": {"session_id": "user_1"}}
)
print("Turn 2:", res2.content)
