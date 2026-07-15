from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import CharacterTextSplitter

# Choosing the right chunk size and overlap is crucial and depends on your embedding model
# and the type of questions you expect users to ask.

with open("sample_data/sample.txt", "r") as f:
    text = f.read()

# Scenario A: Tiny chunks (High precision, low context)
tiny_splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=50,
    chunk_overlap=0
)
tiny_chunks = tiny_splitter.create_documents([text])

# Scenario B: Large chunks with overlap (Lower precision, high context)
large_splitter = CharacterTextSplitter(
    separator=" ",
    chunk_size=400,
    chunk_overlap=100
)
large_chunks = large_splitter.create_documents([text])

print(f"Tiny Splitter created {len(tiny_chunks)} chunks.")
print(f"Large Splitter created {len(large_chunks)} chunks.\n")

print("Notice how a tiny chunk might not contain enough info to answer a question:")
print(f"Tiny Chunk 1: {tiny_chunks[0].page_content}")
print(f"Tiny Chunk 2: {tiny_chunks[1].page_content}")
