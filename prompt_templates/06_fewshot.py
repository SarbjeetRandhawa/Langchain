from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate,
)

# 1. Define your examples
examples = [
    {"input": "2+2", "output": "4"},
    {"input": "2+3", "output": "5"},
    {"input": "3+4", "output": "7"},
]

# 2. Define how each example should be formatted
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

# 3. Create the few-shot prompt template using the examples and the formatter
few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

print("--- Few Shot Prompt Only ---")
print(few_shot_prompt.format())
print("-" * 40)

# 4. Assemble the final prompt, inserting the few-shot template where appropriate
final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a wondrous wizard of math."),
        few_shot_prompt,
        ("human", "{question}"),
    ]
)

print("\n--- Final Prompt String ---")
print(final_prompt.format(question="What is 5+5?"))
print("-" * 40)

# Invoke the prompt to get the list of messages
chat_prompt = final_prompt.invoke({"question": "What is 5+5?"})

print("\n--- Message Objects ---")
for message in chat_prompt.messages:
    print(f"{message.type.capitalize()}: {message.content}")
