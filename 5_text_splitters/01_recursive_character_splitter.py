from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load our sample text
with open("sample_data/sample.txt", "r") as f:
    text = f.read()

# 1. Initialize the splitter
# It tries to split on double newline (paragraphs), then single newline (sentences), 
# then space (words), then empty string (characters).
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,    # Maximum size of chunks to return
    chunk_overlap=50,  # Overlap in characters between chunks to maintain context
    length_function=len,
    is_separator_regex=False,
)

# 2. Split the text
chunks = splitter.create_documents([text])

# 3. Inspect the chunks
print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i+1} (Length: {len(chunk.page_content)}) ---")
    print(chunk.page_content)
    print()
