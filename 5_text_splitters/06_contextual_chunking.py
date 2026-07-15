from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Contextual chunking involves appending global context (like a document title or summary)
# directly into the chunk's content or metadata before embedding it.

with open("sample_data/sample.txt", "r") as f:
    text = f.read()

document_title = "Introduction to LangChain and Text Splitting"

splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=20)
chunks = splitter.create_documents([text])

print("--- Standard Chunk (Loses context if separated from document) ---")
print(chunks[0].page_content)
print("\n")

print("--- Contextual Chunk (Retains context even in isolation) ---")
# We manually prepend the document title to the content of each chunk.
# When this chunk is embedded, the vector will capture the global context (the title)
# as well as the local context (the chunk text).
for chunk in chunks:
    chunk.page_content = f"Document Title: {document_title}\n\n{chunk.page_content}"

print(chunks[0].page_content)
