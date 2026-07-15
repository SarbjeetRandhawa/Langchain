from dotenv import load_dotenv
load_dotenv()

from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings 

# Load our sample text
with open("sample_data/sample.txt", "r") as f:
    text = f.read()

# 1. Initialize an embedding model
# Semantic chunking requires an embedding model to measure sentence similarity!
# We'll use Google Generative AI embeddings for this example.
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# 2. Initialize the Semantic Chunker
# It splits on sentences, then clusters them based on embedding similarity.
# When the similarity drops below a certain threshold, it starts a new chunk.
# Note: You may need to run `pip install langchain_experimental` for this to work.
try:
    splitter = SemanticChunker(
        embeddings,
        breakpoint_threshold_type="percentile" # "percentile", "standard_deviation", "interquartile"
    )

    # 3. Split the text
    chunks = splitter.create_documents([text])

    # 4. Inspect the chunks
    print(f"Total semantic chunks created: {len(chunks)}\n")

    for i, chunk in enumerate(chunks):
        print(f"--- Chunk {i+1} ---")
        print(chunk.page_content)
        print()
except Exception as e:
    print(f"Error: {e}")
    print("Ensure you have the required packages installed: pip install langchain-experimental langchain-google-genai")
