from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

 
history = [
    HumanMessage(content="Hi"),
    AIMessage(content="Hello! How can I help?"),

    HumanMessage(content="My name is Sanjeev."),
    AIMessage(content="Nice to meet you, Sanjeev.")
]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{question}"),
])

chat_prompt = prompt.invoke({"history": history, "question": "What is my name?"})

messages = chat_prompt.to_messages()

for message in messages:
    print(type(message).__name__)
    print(message.content)
    print("-" * 40)