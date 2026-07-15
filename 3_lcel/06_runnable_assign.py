from dotenv import load_dotenv
load_dotenv()

from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

# RunnableAssign is typically used via the .assign() method on RunnablePassthrough. 
# It takes an input dictionary, runs some operations, and ADDS the results 
# to that dictionary, returning the combined dictionary.

model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

# Let's say our initial input is a dictionary with a "topic"
# We want to first generate a joke about the topic, and then a translation of that joke.

joke_prompt = ChatPromptTemplate.from_template("Tell me a joke about {topic}")
translate_prompt = ChatPromptTemplate.from_template("Translate this joke to Spanish:\n\n{joke}")

joke_chain = joke_prompt | model | output_parser
translate_chain = translate_prompt | model | output_parser

# Here we use .assign() to add the "joke" key to our input dictionary
chain = (
    RunnablePassthrough.assign(joke=joke_chain)
    # At this point, the output is a dict: {"topic": "...", "joke": "..."}
    # Now we can use the "joke" key in our next step
    .assign(spanish_translation=translate_chain)
)

# We start with just a topic
response = chain.invoke({"topic": "penguins"})

print(f"Original Topic: {response['topic']}\n")
print(f"Joke:\n{response['joke']}\n")
print(f"Spanish Translation:\n{response['spanish_translation']}")
