from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader

# 1. Initialize the loader with the path to the text file
file_path = "sample_data/sample.txt"
loader = TextLoader(file_path)

# 2. Load the documents
# This returns a list of Document objects. Since it's a single text file, 
# it will return a list with exactly one Document inside it.
documents = loader.load()

# 3. Inspect the loaded document
print(f"Loaded {len(documents)} document(s)\n")

for doc in documents:
    print("--- Metadata ---")
    print(doc.metadata)
    print("\n--- Content ---")
    print(doc.page_content)
