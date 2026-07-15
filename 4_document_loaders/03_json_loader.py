from dotenv import load_dotenv
load_dotenv()

# Note: The standard LangChain JSONLoader requires the 'jq' python package to be installed.
# If you don't have it, run: pip install jq
from langchain_community.document_loaders import JSONLoader

file_path = "sample_data/sample.json"

# We use a jq schema to tell the loader how to parse the JSON.
# '.[].text' means: iterate over the array at the root, and extract the 'text' field.
loader = JSONLoader(
    file_path=file_path,
    jq_schema='.[].text',
    text_content=True
)

try:
    documents = loader.load()
    print(f"Loaded {len(documents)} document(s) from JSON\n")
    
    for i, doc in enumerate(documents):
        print(f"--- Document {i+1} ---")
        print(f"Metadata: {doc.metadata}")
        print(f"Content:\n{doc.page_content}\n")
except Exception as e:
    print(f"Error loading JSON. Did you install 'jq'? Run 'pip install jq'.\nError: {e}")
