from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnableBranch
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# RunnableBranch allows you to add conditional logic (if/else/elif) to your chains.
# It evaluates a set of conditions and runs the first branch that returns True.

model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

# 1. Define the branches (different prompts based on the topic)
math_prompt = ChatPromptTemplate.from_template("You are a math genius. Answer this: {question}")
history_prompt = ChatPromptTemplate.from_template("You are a historian. Answer this: {question}")
general_prompt = ChatPromptTemplate.from_template("You are a helpful assistant. Answer this: {question}")

math_chain = math_prompt | model | output_parser
history_chain = history_prompt | model | output_parser
general_chain = general_prompt | model | output_parser

# 2. Define the classification step
# We'll use the LLM to classify the question first.
classification_prompt = ChatPromptTemplate.from_template(
    "Classify the following question as either 'math', 'history', or 'general'. "
    "Respond with ONLY ONE word.\nQuestion: {question}"
)
classifier_chain = classification_prompt | model | output_parser

# 3. Create the branching logic
# RunnableBranch takes a sequence of (condition, runnable) pairs, and a final default runnable.
branch = RunnableBranch(
    # (Condition, Chain to run if True)
    (lambda x: "math" in x["topic"].lower(), math_chain),
    (lambda x: "history" in x["topic"].lower(), history_chain),
    # Default chain if no conditions match
    general_chain
)

# 4. Put it all together using RunnablePassthrough.assign to keep the original question
full_chain = (
    RunnablePassthrough.assign(topic=classifier_chain) 
    | branch
)

# Test it out!
question1 = "What is the square root of 144?"
question2 = "When was the Declaration of Independence signed?"
question3 = "What is a good recipe for chocolate chip cookies?"

print(f"--- Q: {question1} ---")
print(full_chain.invoke({"question": question1}))

print(f"\n--- Q: {question2} ---")
print(full_chain.invoke({"question": question2}))

print(f"\n--- Q: {question3} ---")
print(full_chain.invoke({"question": question3}))
