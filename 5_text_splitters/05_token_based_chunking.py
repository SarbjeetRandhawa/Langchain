from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import TokenTextSplitter

# Token-based splitters are useful because LLM limits (and pricing) are based on tokens, 
# not characters. A token is roughly 3/4 of a word in English.

with open("sample_data/sample.txt", "r") as f:
    text = f.read()

# Note: TokenTextSplitter requires the 'tiktoken' library. 
# Run 'pip install tiktoken' if you haven't already.
try:
    # 1. Initialize the Token Splitter
    # We specify chunk_size in TOKENS, not characters.
    splitter = TokenTextSplitter(
        chunk_size=50, 
        chunk_overlap=10
    )

    # 2. Split the text
    chunks = splitter.create_documents([text])

    # 3. Inspect
    print(f"Total token chunks created: {len(chunks)}\n")

    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk.page_content)
        print()
except ImportError:
    print("Please install tiktoken to run this script: pip install tiktoken")
