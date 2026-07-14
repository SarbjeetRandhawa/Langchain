from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import MessagesPlaceholder


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI assistant for {company}.

Today's date is {date}.
"""
        ),

        ("human", "{question}")
    ]
)

print(prompt.input_variables)


partial_prompt = prompt.partial(
    company="MutualArt",
    date="14 July 2026"
)
print(partial_prompt.input_variables)


chat_prompt = partial_prompt.invoke(
    {
        "question": "Explain LangChain."
    }
)

print(chat_prompt.to_string())



