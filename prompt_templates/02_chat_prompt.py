from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{question}"),
])
print(prompt + "/n/n/n/n")
print(type(prompt))

chat_prompt= prompt.invoke({"question": "What is the capital of France?"})
print(chat_prompt.to_messages())
print(type(chat_prompt))

message  = chat_prompt.messages
print(message)

# Print the content of the message
print(message[0].content)
print(message[1].content)


