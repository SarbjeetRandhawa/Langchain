from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter

# Parent-Child chunking is usually handled at the Retriever level (ParentDocumentRetriever).
# However, the concept relies on creating two splitters: a parent splitter (large chunks)
# and a child splitter (small chunks).

with open("sample_data/sample.txt", "r") as f:
    text = f.read()

# 1. Parent Splitter (Large chunks for context)
parent_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0
)
parent_chunks = parent_splitter.create_documents([text])

# 2. Child Splitter (Small chunks for precise search)
child_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

print(f"Generated {len(parent_chunks)} Parent Chunks.\n")

# Normally, you would use a ParentDocumentRetriever to automate linking the child
# to the parent. Here is how they are split conceptually:

for i, parent in enumerate(parent_chunks):
    print(f"=== PARENT CHUNK {i+1} ===")
    print(parent.page_content)
    
    # Split the parent into children
    children = child_splitter.create_documents([parent.page_content])
    print(f"\n  -> Split into {len(children)} Child Chunks:")
    
    for j, child in enumerate(children):
        print(f"    - Child {j+1}: {child.page_content[:50]}...")
    print("\n")
