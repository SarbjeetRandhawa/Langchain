from langchain.memory import ConversationBufferWindowMemory

# k=1 means it only remembers the last interaction (1 user + 1 AI message)
memory = ConversationBufferWindowMemory(k=1)
memory.save_context({"input": "hi"}, {"output": "whats up"})
memory.save_context({"input": "not much you"}, {"output": "not much"})

# Will only return the second interaction
print(memory.load_memory_variables({}))
