# Langchain

<details>
  <summary>✅ Phase 1 - Why LangChain Exists</summary>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b> LangChain provides a standard interface for building applications powered by LLMs. Before LangChain, developers had to write custom boilerplate code to connect to different LLM providers, manage complex prompts, parse outputs manually, and handle context windows. LangChain abstracts away all of this complexity into a unified framework. It makes it incredibly simple to build robust, production-ready applications like RAG (Retrieval-Augmented Generation) systems, dynamic agents, and complex chatbots by providing built-in orchestration, prompt management, memory, and tool-calling capabilities out of the box.<br>
  </details>
<details>
  <summary>✅ Phase 2 - Core Components & Runnables</summary>
  <br>
  &nbsp;&nbsp;&nbsp; &bull; LangChain Architecture<br>
  &nbsp;&nbsp;&nbsp; &bull; Runnable (Most Important)<br>
  &nbsp;&nbsp;&nbsp; &bull; Chat Models<br>
  &nbsp;&nbsp;&nbsp; &bull; invoke()<br>
  &nbsp;&nbsp;&nbsp; &bull; batch()<br>
  &nbsp;&nbsp;&nbsp; &bull; stream()<br>
  &nbsp;&nbsp;&nbsp; &bull; ainvoke()<br>
  &nbsp;&nbsp;&nbsp; &bull; Messages<br>
  &nbsp;&nbsp;&nbsp; &bull; Response Objects<br>
  &nbsp;&nbsp;&nbsp; &bull; Summary<br>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b> The foundational elements of LangChain revolve around the <i>Runnable</i> interface, which allows components (like Chat Models) to be easily chained together using the pipe operator (`|`). This uniform interface natively supports standard synchronous methods like `invoke()`, `batch()`, and `stream()`, as well as their asynchronous counterparts like `ainvoke()`. Chat Models interact using standard `Messages` (System, Human, AI) and return structured `Response Objects`.<br>
  </details>
<details>
  <summary>✅ Phase 3 - Prompt Templates</summary>
  <br>
  &nbsp;&nbsp;&nbsp; &bull; PromptTemplate<br>
  &nbsp;&nbsp;&nbsp; &bull; ChatPromptTemplate<br>
  &nbsp;&nbsp;&nbsp; &bull; Messages<br>
  &nbsp;&nbsp;&nbsp; &bull; MessagesPlaceholder<br>
  &nbsp;&nbsp;&nbsp; &bull; Partial Formatting<br>
  &nbsp;&nbsp;&nbsp; &bull; FewShotPromptTemplate<br>
  &nbsp;&nbsp;&nbsp; &bull; Dynamic Few-shot PromptTemplate<br>
  </details>
<details>
  <summary>✅ Phase 4 - Output Parsers</summary>
  <br>
  &nbsp;&nbsp;&nbsp; &bull; StrOutputParser ⭐<br>
  &nbsp;&nbsp;&nbsp; &bull; JsonOutputParser ⭐⭐⭐⭐⭐<br>
  &nbsp;&nbsp;&nbsp; &bull; PydanticOutputParser ⭐⭐⭐⭐⭐<br>
  &nbsp;&nbsp;&nbsp; &bull; OutputFixingParser ⭐⭐⭐⭐<br>
  &nbsp;&nbsp;&nbsp; &bull; RetryOutputParser ⭐⭐⭐⭐<br>
  &nbsp;&nbsp;&nbsp; &bull; CommaSeparatedListOutputParser<br>
  &nbsp;&nbsp;&nbsp; &bull; MarkdownListOutputParser<br>
  &nbsp;&nbsp;&nbsp; &bull; NumberedListOutputParser<br>
  &nbsp;&nbsp;&nbsp; &bull; Custom Output Parsers
  </details>
<details>
  <summary>✅ Phase 5 - LCEL ⭐⭐⭐⭐⭐</summary>
  <br>
  &nbsp;&nbsp;&nbsp; &bull;  What is LCEL?<br>
  &nbsp;&nbsp;&nbsp; &bull;  RunnableSequence (the `|` operator)<br>
  &nbsp;&nbsp;&nbsp; &bull;  RunnableLambda<br>
  &nbsp;&nbsp;&nbsp; &bull;  RunnablePassthrough<br>
  &nbsp;&nbsp;&nbsp; &bull;  RunnableParallel<br>
  &nbsp;&nbsp;&nbsp; &bull;  RunnableAssign<br>
  &nbsp;&nbsp;&nbsp; &bull;  RunnableBranch<br>
  &nbsp;&nbsp;&nbsp; &bull;  LCEL Execution (invoke, batch, stream)<br>
  &nbsp;&nbsp;&nbsp; &bull;  Building Complete AI Pipelines<br>
  &nbsp;&nbsp;&nbsp; &bull;  Production Patterns<br>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b>
  <ul style="padding-left: 40px;">
    <li style="margin-bottom: 10px;"><b>Execution Methods:</b> LCEL runnables support various execution methods. `invoke()` is used for single inputs, returning the final output. `batch()` processes a list of inputs concurrently, optimizing for speed. `stream()` yields chunks of the output as soon as they are available, crucial for building responsive UIs.</li>
    <li style="margin-bottom: 10px;"><b>Building Pipelines:</b> Combining different LCEL components (prompts, models, parsers, runnables) allows you to build complex AI pipelines. You can seamlessly chain multiple steps, routing inputs based on conditions (RunnableBranch), or running tasks concurrently (RunnableParallel).</li>
    <li><b>Production Patterns:</b> In production, LCEL simplifies adding fallback models, retry logic (using RetryOutputParser), and observability. Because of its standard interface, integrating LangSmith for tracing and debugging comes almost for free.</li>
  </ul>
  </details>
<details>
  <summary>✅ Phase 6 - Chains</summary>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b> The legacy `Chain` classes (like `LLMChain`, `SequentialChain`, etc.) were the original way to build applications in LangChain before LCEL was introduced. Today, almost all of these legacy chains are deprecated in favor of LCEL runnables. We learn about these older chains primarily so we can read, understand, and migrate legacy codebases and older projects to the modern LCEL standard.<br><br>
  
  <table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th style="padding: 8px; border: 1px solid #ddd;">Chain</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Status</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Modern Equivalent</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">LLMChain</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;"><code>prompt | llm | parser</code></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">ConversationChain</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Prompt + Memory + LCEL</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">SequentialChain</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;"><code>chain1 | chain2</code></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">RouterChain</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;"><code>RunnableBranch</code></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">TransformChain</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;"><code>RunnableLambda</code></td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">RetrievalQA</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Retriever + Prompt + LLM</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">ConversationalRetrievalChain</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Deprecated</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Retriever + Memory + Prompt</td>
      </tr>
    </tbody>
  </table>

  </details>
<details>
  <summary>✅ Phase 7 - Document Loaders</summary>
  <br>
  &nbsp;&nbsp;&nbsp; &bull; Introduction to Document Loaders<br>
  &nbsp;&nbsp;&nbsp; &bull; TextLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; PyPDFLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; PyMuPDFLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; CSVLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; JSONLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; WebBaseLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; DirectoryLoader<br>
  &nbsp;&nbsp;&nbsp; &bull; Lazy Loading & Async Loading<br>
  &nbsp;&nbsp;&nbsp; &bull; Custom Document Loaders<br>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b>
  <ul style="padding-left: 40px;">
    <li style="margin-bottom: 10px;"><b>TextLoader:</b> The simplest loader, reads raw text from `.txt` files or simple string files.</li>
    <li style="margin-bottom: 10px;"><b>PyPDFLoader & PyMuPDFLoader:</b> Used for extracting text and metadata from PDF files. PyMuPDFLoader is often much faster and extracts more precise metadata than standard PyPDF.</li>
    <li style="margin-bottom: 10px;"><b>CSVLoader:</b> Loads tabular data from CSVs where each row becomes a Document, typically mapping columns to metadata or content.</li>
    <li style="margin-bottom: 10px;"><b>JSONLoader:</b> Parses structured JSON data using `jq` schemas to extract specific fields into Document objects.</li>
    <li style="margin-bottom: 10px;"><b>WebBaseLoader:</b> Scrapes HTML from given URLs and extracts the text content, often stripping out raw HTML tags.</li>
    <li style="margin-bottom: 10px;"><b>DirectoryLoader:</b> A powerful wrapper that can load all files in a folder, applying specific loaders (like TextLoader or PyPDFLoader) based on file extensions.</li>
    <li style="margin-bottom: 10px;"><b>Lazy & Async Loading:</b> Modern patterns for memory efficiency. Instead of loading thousands of files into RAM at once, you yield them one by one (`lazy_load()`) or load them concurrently (`alazy_load()`).</li>
    <li><b>Custom Loaders:</b> For proprietary formats or databases, you can build custom loaders by subclassing `BaseLoader` and defining how to yield `Document` objects.</li>
  </ul>
  </details>
  
<details>
  <summary>✅ Phase 8 - Text Splitters</summary>
  <br>
  <dl><dd>
  <details>
    <summary> Introduction to Text Splitters</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Text Splitters break large documents into smaller chunks so they fit into the context window of LLMs. This is a critical step for RAG (Retrieval-Augmented Generation) to ensure the LLM receives highly relevant snippets instead of entire books.
    </div>
  </details>
  
  <details>
    <summary> CharacterTextSplitter</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The simplest splitter. It splits text based on a single character (usually a newline `\n\n`) and measures chunk size by the number of characters.
    </div>
  </details>
  
  <details>
    <summary> RecursiveCharacterTextSplitter ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The recommended splitter for generic text. It tries to split on paragraphs (`\n\n`), then sentences (`\n`), then words (` `), and finally characters (`""`) to keep semantically related pieces of text together as much as possible while strictly enforcing the chunk size.
    </div>
  </details>
  
  <details>
    <summary> TokenTextSplitter</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Splits text by token count rather than character count, ensuring chunks fit perfectly into LLM context windows (since LLMs charge and limit based on tokens, not characters). Often uses Tiktoken under the hood.
    </div>
  </details>
  
  <details>
    <summary> Markdown & HTML Splitters</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> These splitters understand document structure. `MarkdownHeaderTextSplitter` splits based on headers (e.g., `#`, `##`) and adds the header info to the chunk's metadata. `HTMLHeaderTextSplitter` does the same for `<h1>`, `<h2>`, etc.
    </div>
  </details>
  
  <details>
    <summary> Code Splitters</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> `PythonCodeTextSplitter` (and others) understand programming language syntax. They split along functions, classes, and logical code blocks instead of just newlines, which prevents breaking a function in half.
    </div>
  </details>
  
  <details>
    <summary> Semantic Chunking ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> An advanced method that uses embedding models to measure the similarity between sentences. It groups sentences into chunks based on semantic meaning, creating a new chunk only when the topic naturally shifts.
    </div>
  </details>
  
  <details>
    <summary> Parent-Child Chunking ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> (Also known as Auto-merging Retriever). You split documents into small "child" chunks for precise retrieval, but link them to a larger "parent" chunk. If enough children are retrieved, the LLM is fed the entire parent chunk to provide broader context.
    </div>
  </details>
  
  <details>
    <summary> Contextual Chunking</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Involves appending global context (like the document title or a summary of the whole page) to every single chunk so that isolated chunks don't lose their underlying meaning during retrieval.
    </div>
  </details>
  
  <details>
    <summary> Choosing Chunk Size & Overlap ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Chunk size dictates how much info is in a chunk (e.g., 1000 characters). Chunk overlap dictates how much the end of chunk A overlaps with the beginning of chunk B (e.g., 200 characters). Overlap is crucial to ensure concepts at the boundary of a chunk aren't cut in half.
      <br><br>
      <b>How do you decide chunk size and overlap?</b><br>
      Choose a chunk size that captures one coherent concept while remaining small enough for accurate embeddings. Add a modest overlap (typically around 10–20%) so concepts spanning chunk boundaries are preserved. The exact values depend on the document type, embedding model, and the kinds of questions users are expected to ask.
      <br><br>
      <b>Production Recommendations:</b>
      <table border="1" style="border-collapse: collapse; width: 100%; text-align: left; margin-top: 10px; margin-bottom: 10px;">
        <thead>
          <tr style="background-color: #f2f2f2;">
            <th style="padding: 8px; border: 1px solid #ddd;">Document Type</th>
            <th style="padding: 8px; border: 1px solid #ddd;">Chunk Size</th>
            <th style="padding: 8px; border: 1px solid #ddd;">Overlap</th>
          </tr>
        </thead>
        <tbody>
          <tr><td style="padding: 8px; border: 1px solid #ddd;">FAQs</td><td style="padding: 8px; border: 1px solid #ddd;">150–300</td><td style="padding: 8px; border: 1px solid #ddd;">20–40</td></tr>
          <tr><td style="padding: 8px; border: 1px solid #ddd;">API Docs</td><td style="padding: 8px; border: 1px solid #ddd;">300–600</td><td style="padding: 8px; border: 1px solid #ddd;">50–100</td></tr>
          <tr><td style="padding: 8px; border: 1px solid #ddd;">Technical Docs</td><td style="padding: 8px; border: 1px solid #ddd;">500–800</td><td style="padding: 8px; border: 1px solid #ddd;">75–150</td></tr>
          <tr><td style="padding: 8px; border: 1px solid #ddd;">Research Papers</td><td style="padding: 8px; border: 1px solid #ddd;">700–1200</td><td style="padding: 8px; border: 1px solid #ddd;">100–200</td></tr>
          <tr><td style="padding: 8px; border: 1px solid #ddd;">Books</td><td style="padding: 8px; border: 1px solid #ddd;">800–1500</td><td style="padding: 8px; border: 1px solid #ddd;">150–250</td></tr>
          <tr><td style="padding: 8px; border: 1px solid #ddd;">Legal Contracts</td><td style="padding: 8px; border: 1px solid #ddd;">1000–2000</td><td style="padding: 8px; border: 1px solid #ddd;">150–300</td></tr>
        </tbody>
      </table>
      <i>*Treat these as starting points. The best settings come from evaluating retrieval quality on your own data.</i>
    </div>
  </details>
  
  <details>
    <summary> Best Practices & Common Mistakes</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Common mistakes include setting overlap to 0 (losing context at boundaries), using CharacterTextSplitter for complex documents, or not testing whether the chunk size actually captures enough information for the LLM to answer questions.
    </div>
  </details>
  </dd></dl>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Common Types of Text Splitters:</b> LangChain provides several strategies:<br><br>
  
  <table border="1" style="border-collapse: collapse; width: 100%; text-align: left;">
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th style="padding: 8px; border: 1px solid #ddd;">Splitter</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Splits By</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Use Case</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">CharacterTextSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Fixed characters</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Simple text</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">RecursiveCharacterTextSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Multiple separators</td>
        <td style="padding: 8px; border: 1px solid #ddd;">⭐ Most common</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">TokenTextSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Tokens</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Token-aware chunking</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">MarkdownHeaderTextSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Markdown headings</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Markdown docs</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">HTMLHeaderTextSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">HTML tags</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Websites</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">PythonCodeTextSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Python syntax</td>
        <td style="padding: 8px; border: 1px solid #ddd;">Source code</td>
      </tr>
      <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">RecursiveJsonSplitter</td>
        <td style="padding: 8px; border: 1px solid #ddd;">JSON structure</td>
        <td style="padding: 8px; border: 1px solid #ddd;">JSON documents</td>
      </tr>
    </tbody>
  </table>

</details>

<details>
  <summary>✅ Phase 9 - Embeddings</summary>
  <br>
  <dl><dd>
    Lesson 1 Introduction to Embeddings<br><br>
    Lesson 2 → How Embeddings Are Created (Training Process)<br><br>
    Lesson 3 → High-Dimensional Vector Space<br><br>
    Lesson 4 → Similarity Metrics<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; Cosine Similarity ⭐⭐⭐⭐⭐<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; Dot Product<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; Euclidean Distance<br><br>
    Lesson 5 → Popular Embedding Models<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; BGE<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; E5<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; OpenAI<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&bull; Sentence Transformers<br><br>
    Lesson 6 → Choosing the Right Embedding Model<br><br>
    Lesson 7 → Embedding Pitfalls & Best Practices<br><br>
    Lesson 8 → LangChain Embedding Interfaces (Coding)<br>
  </dd></dl>
</details>
<details>
  <summary>✅ Phase 10 - Vector Stores</summary>
  <br>
  <dl><dd>
  <details>
    <summary> What is a Vector Store</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A specialized database designed to store, manage, and query high-dimensional vectors (embeddings) efficiently. They allow for fast similarity search across massive datasets.
    </div>
  </details>
  
  <details>
    <summary> Why SQL Isn't Enough</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> SQL and traditional relational databases are built for exact matches (e.g., `WHERE author = 'John'`). Vector databases are built for similarity searches (finding the closest points in space), which traditional databases struggle to do efficiently at scale without specialized extensions.
    </div>
  </details>
  
  <details>
    <summary> Exact Search vs ANN</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Exact Search (k-NN) compares a query against every single vector in the database. It's 100% accurate but too slow for millions of records. ANN (Approximate Nearest Neighbors) trades a tiny bit of accuracy for massive speed gains by organizing vectors into optimized, easily searchable structures.
    </div>
  </details>
  
  <details>
    <summary> HNSW ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Hierarchical Navigable Small World. The most popular and state-of-the-art ANN algorithm. It builds a multi-layered graph where top layers have long links for fast zooming in, and bottom layers have short links for fine-tuning the search. It is extremely fast and accurate.
    </div>
  </details>
  
  <details>
    <summary> FAISS</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Facebook AI Similarity Search. A powerful, low-level library for efficient similarity search and clustering. It typically runs locally in-memory, making it excellent for prototyping or small-to-medium datasets.
    </div>
  </details>
  
  <details>
    <summary> Chroma</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> An open-source, AI-native embedding database. It is incredibly popular for local development and simple RAG projects because it is trivial to set up and can run completely locally.
    </div>
  </details>
  
  <details>
    <summary> Qdrant ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A high-performance, open-source vector search engine written in Rust. It offers production-grade features, excellent horizontal scaling, and advanced payload (metadata) filtering. Highly recommended for robust production applications.
    </div>
  </details>
  
  <details>
    <summary> Pinecone</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A fully managed, cloud-native vector database. It is closed-source but extremely easy to use for production since you don't have to manage any infrastructure yourself.
    </div>
  </details>
  
  <details>
    <summary> Metadata Filtering</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Vector databases allow you to attach metadata (like date, author, or category) to your embeddings. During retrieval, you can filter by this metadata (e.g., "Find similar documents BUT only from 2024") to drastically improve both accuracy and query speed.
    </div>
  </details>
  
  <details>
    <summary> LangChain Vector Stores</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> LangChain provides a unified `VectorStore` interface. This means you can swap out FAISS, Qdrant, or Pinecone by just changing one line of code during initialization, while the rest of your retrieval logic (`.similarity_search()`) stays exactly the same.
    </div>
  </details>
  </dd></dl>
</details>

<details>
  <summary>✅ Phase 11 - Retrievers</summary>
  <br>
  <dl><dd>
  <details>
    <summary> What is a Retriever?</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A Retriever is an interface that returns documents given an unstructured query. It is more general than a vector store. While a vector store is a database that can retrieve vectors, a Retriever can be anything (e.g., a Wikipedia search, an API call) that takes in a string and returns a list of relevant Documents.
    </div>
  </details>

  <details>
    <summary> VectorStoreRetriever ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The most common type of retriever in LangChain. It is a lightweight wrapper around a Vector Store (like Qdrant or Pinecone) that conforms to the Retriever interface. Under the hood, it takes your query, embeds it using an embedding model, and performs a similarity search in the underlying vector database to fetch the most relevant chunks.
    </div>
  </details>

  <details>
    <summary> Similarity Search</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The standard method used by VectorStoreRetrievers. It simply measures the mathematical distance (like Cosine Similarity) between the query vector and document vectors, returning the top K closest matches.
    </div>
  </details>
  
  <details>
    <summary> Similarity Score Threshold</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A retrieval method that lets you set a minimum similarity score. Instead of always returning a fixed number of documents (like top 4), it returns all documents that score above the threshold (e.g., > 0.8), ensuring that irrelevant documents aren't passed to the LLM.
    </div>
  </details>

  <details>
    <summary> MMR Retriever</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Maximum Marginal Relevance (MMR). It tries to optimize for both relevance to the query AND diversity among the retrieved documents. This prevents returning 5 documents that all say the exact same thing, ensuring a wider context is captured.
    </div>
  </details>

  <details>
    <summary> MultiQuery Retriever ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> An advanced retriever that uses an LLM to generate multiple variations of the user's original query. It then performs a retrieval for *each* variation, combines the results, and removes duplicates. This is incredibly powerful because it overcomes the limitations of distance-based search where a slightly differently worded query might miss the right document.
    </div>
  </details>

  <details>
    <summary> Contextual Compression Retriever ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Sometimes relevant documents contain a lot of useless filler text that wastes the LLM's context window. This retriever solves that by using an LLM (or a smaller model) to "compress" or filter the retrieved documents, extracting only the exact sentences or paragraphs that answer the query before passing them to the final LLM.
    </div>
  </details>

  <details>
    <summary> Parent Document Retriever ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> One of the most effective retrieval strategies. It splits documents into small "child" chunks for highly accurate, precise similarity search. However, instead of passing the small child chunk to the LLM (which might lack surrounding context), it retrieves the larger "parent" chunk that the child belongs to. This gives you the best of both worlds: the precision of small chunks and the rich context of large chunks.
    </div>
  </details>

  <details>
    <summary> Ensemble Retriever (Hybrid Search) ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Combines the results of multiple different retrievers. The most common pattern is "Hybrid Search", which pairs a sparse keyword-based retriever (like BM25, which looks for exact word matches) with a dense vector retriever (which looks for semantic meaning). It then uses algorithms like Reciprocal Rank Fusion (RRF) to re-rank the combined results, providing vastly superior accuracy over using either method alone.
    </div>
  </details>

  <details>
    <summary> Self-Query Retriever ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A very smart retriever that uses an LLM to parse the user's natural language query into two parts: a semantic search string and a structured metadata filter. For example, if the user asks "What are some good sci-fi movies from 2023?", the LLM extracts "good sci-fi movies" for the vector search and creates a strict filter `year == 2023` for the metadata. This dramatically improves retrieval accuracy when dealing with structured attributes.
    </div>
  </details>

  <details>
    <summary> Time-Weighted Retriever</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> A retriever that combines semantic similarity with recency. Documents gradually "decay" in score over time, meaning newer documents are favored over older ones unless the older document is significantly more relevant.
    </div>
  </details>

  <details>
    <summary> MultiVector Retriever</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Allows you to store multiple vectors per document. For example, you can create vectors for the document's summary, its title, and its sub-sections, but all of them point back to the same full document during retrieval.
    </div>
  </details>
  </dd></dl>
</details>
<details>
  <summary>✅ Phase 12 - Memory</summary>
  <br>
  <dl><dd>
  <details>
    <summary> What is Memory?</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Memory is the ability of an LLM system to remember previous interactions. By default, LLMs are stateless; they don't remember what you said in the previous prompt. Memory components in LangChain intercept user inputs and model outputs, storing them so they can be injected into the context of future conversations.
    </div>
  </details>

  <details>
    <summary> Chat Message History ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The core abstraction that stores the actual sequence of messages (Human, AI, System). It is the raw database of a conversation. While you can store this in memory for testing, in production you typically back this with a database (like Redis, Postgres, or MongoDB) using integrations like `RedisChatMessageHistory` so conversations survive server restarts.
    </div>
  </details>

  <details>
    <summary> ConversationBufferMemory</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The simplest form of memory. It just stores a raw, unedited list of all chat messages and passes the entire history into the prompt every time.
    </div>
  </details>

  <details>
    <summary> ConversationBufferWindowMemory</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Keeps a sliding window of the last 'K' messages. Older messages get dropped, preventing the prompt from exceeding the token limit as the conversation grows.
    </div>
  </details>

  <details>
    <summary> ConversationTokenBufferMemory</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Similar to the window memory, but instead of keeping the last K messages, it keeps the maximum number of messages that fit under a specific token count threshold.
    </div>
  </details>

  <details>
    <summary> ConversationSummaryMemory ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Instead of storing the exact raw messages (which quickly eats up tokens), this uses an LLM to actively summarize the conversation as it happens. The summarized text is injected into the prompt as context. This is highly efficient for long-running conversations where you only need the broad strokes of what was discussed, rather than word-for-word accuracy.
    </div>
  </details>

  <details>
    <summary> ConversationSummaryBufferMemory ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> The ultimate hybrid memory for complex chatbots. It keeps the exact raw text of the most recent interactions (the buffer) up to a certain token limit, and once that limit is reached, it summarizes the oldest messages. This gives the LLM perfect short-term memory (for the recent context) and summarized long-term memory, optimizing both token usage and conversational accuracy.
    </div>
  </details>

  <details>
    <summary> VectorStoreRetrieverMemory</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Treats memory like a search problem. It stores past conversation turns in a vector database and retrieves the most semantically relevant past messages for the current turn, rather than just the most recent ones.
    </div>
  </details>

  <details>
    <summary> EntityMemory</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> Automatically extracts entities (names, places, concepts) from the conversation and builds a mini knowledge graph or dictionary about those entities, allowing the LLM to recall specific facts about a user.
    </div>
  </details>

  <details>
    <summary> Memory in LCEL</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> In LCEL, memory is often handled using `RunnableWithMessageHistory`, which automatically fetches historical messages for a given session ID and appends the new interaction to the database.
    </div>
  </details>

  <details>
    <summary> LangGraph Memory (Modern Approach) ⭐⭐⭐⭐⭐</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <b>Theory:</b> As LangChain evolves, standard memory classes (like ConversationBufferMemory) are being replaced by LangGraph. In LangGraph, memory is naturally managed through "state". By using a `checkpointer` (like SqliteSaver), LangGraph automatically persists the entire state of an agent (including messages) across different turns, enabling powerful concepts like time-traveling, pausing, and resuming long-running agents without needing specialized memory classes.
    </div>
  </details>
  </dd></dl>
</details>

<details>
  <summary>✅ Phase 13 - Tools</summary>
  <br>
  <dl><dd>
  &bull; What is a Tool?<br>
  &bull; Tool Calling vs Function Calling<br><br>
  <details>
    <summary> Types of Tools</summary>
    <div style="margin-top: 5px; margin-bottom: 10px;">
      <dl><dd>
      <details>
        <summary> Utility Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Generic, helpful functions like calculators, current time fetchers, or random number generators that assist the LLM in performing deterministic operations.
        </div>
      </details>
      <details>
        <summary> Retrieval Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Tools that fetch context from a knowledge base or vector store. Often used in RAG to grab chunks of relevant private data before generating a final answer.
        </div>
      </details>
      <details>
        <summary> Search Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Web search integrations (e.g., Google Search, DuckDuckGo, Tavily) that allow the LLM to pull real-time or up-to-date information from the internet.
        </div>
      </details>
      <details>
        <summary> API Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Interfaces that connect the LLM to external REST or GraphQL APIs (e.g., weather services, stock tickers, or GitHub) to read or write external data.
        </div>
      </details>
      <details>
        <summary> Database Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Tools that enable the LLM to query structured databases directly (like SQL or Neo4j). The LLM usually writes the query and the tool executes it.
        </div>
      </details>
      <details>
        <summary> File System Tools ⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Allows the LLM to read from, write to, or list files in a local or remote file system. Great for coding assistants or data analysis agents.
        </div>
      </details>
      <details>
        <summary> Code Execution Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Safe sandbox environments (like a Python REPL or E2B) where the LLM can write code, run it, and see the output to solve complex math or data problems dynamically.
        </div>
      </details>
      <details>
        <summary> Communication Tools ⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Tools used to send emails, Slack messages, or SMS. These give the agent the ability to act on the user's behalf to notify others.
        </div>
      </details>
      <details>
        <summary> Human-in-the-Loop Tools ⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Special tools that pause execution to ask a human for approval, feedback, or missing information before proceeding with high-stakes actions.
        </div>
      </details>
      <details>
        <summary> AI/ML Tools ⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Tools that call other AI models (e.g., passing an image to an OCR model, or using a local classifier) to handle tasks the primary LLM can't do natively.
        </div>
      </details>
      <details>
        <summary> Workflow Tools ⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Integrations with automation platforms like Zapier or Make, allowing the LLM to trigger complex, multi-step business workflows.
        </div>
      </details>
      <details>
        <summary> Custom Business Tools ⭐⭐⭐⭐⭐</summary>
        <div style="margin-top: 5px; margin-bottom: 10px;">
          <b>Theory:</b> Proprietary tools you build specifically for your organization (e.g., "RefundCustomerTool" or "UpdateCRMTool") representing your unique business logic.
        </div>
      </details>
      </dd></dl>
    </div>
  </details>
  <br>
  &bull; Built-in LangChain Tools<br>
  &bull; Creating Custom Tools<br>
  &bull; @tool Decorator<br>
  &bull; StructuredTool<br>
  &bull; BaseTool<br>
  &bull; Tool Schemas (Pydantic)<br>
  &bull; Tool Execution Flow<br>
  <details>
    <summary> Tool Errors & Validation</summary>
    <div style="margin-top: 5px; margin-bottom: 10px; margin-left: 20px;">
      &bull; Input Validation<br>
      &bull; Runtime Errors<br>
      &bull; API Errors<br>
      &bull; Network Errors<br>
      &bull; Authentication Errors<br>
      &bull; Timeout Errors<br>
      &bull; Permission Errors<br>
      &bull; Unexpected Exceptions<br>
    </div>
  </details>
  &bull; Toolkits<br>
  &bull; Tool Calling with LCEL<br>
  <details>
    <summary> Tool Calling with LangGraph</summary>
    <div style="margin-top: 5px; margin-bottom: 10px; margin-left: 20px;">
      <b>Graph Components:</b> Every LangGraph application has a Graph consisting of:<br>
      &bull; State<br>
      &bull; Nodes<br>
      &bull; Edges<br>
      &bull; Conditional Edges<br>
      &bull; START / END<br>
    </div>
  </details>
  </dd></dl>
</details>

- ➡️ Phase 14 - Agents
- ➡️ Phase 15 - Callbacks
- ➡️ Phase 16 - LangSmith & Production
- ➡️ Phase 17 - Build an end-to-end production RAG system