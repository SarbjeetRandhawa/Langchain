from langchain_core.prompts import PromptTemplate

# Create the template
prompt = PromptTemplate.from_template(
    """
You are an AI Tutor.

Answer the following question.

Question:
{question}
"""
)

print(prompt)
print(type(prompt))
# print(prompt.invoke({"question": "What is the capital of France?"}))

print(prompt.format(question="What is the capital of France?"))



# --------------------------------------

template = PromptTemplate.from_template ("""
Language:
{language}

Question:
{question}
""")

print(template.format(language="English", question="What is the capital of France?"))