from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import CSVLoader

# 1. Initialize the CSV loader
file_path = "sample_data/sample.csv"
loader = CSVLoader(file_path=file_path)

# 2. Load the documents
# CSVLoader creates one Document for each row in the CSV file!
documents = loader.load()

# 3. Inspect the loaded documents
print(f"Loaded {len(documents)} document(s) (one for each row in the CSV)\n")

for i, doc in enumerate(documents):
    print(f"--- Document {i+1} ---")
    print(f"Metadata: {doc.metadata}")
    print(f"Content:\n{doc.page_content}\n")
