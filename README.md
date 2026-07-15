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
  &nbsp;&nbsp;&nbsp; &bull; Introduction to Document Loaders ✅<br>
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
- ➡️ Phase 8 - Text Splitters
- ➡️ Phase 9 - Embeddings
- ➡️ Phase 10 - Vector Stores
- ➡️ Phase 11 - Retrievers
- ➡️ Phase 12 - Memory
- ➡️ Phase 13 - Tools
- ➡️ Phase 14 - Agents
- ➡️ Phase 15 - Callbacks
- ➡️ Phase 16 - LangSmith & Production
- ➡️ Phase 17 - Build an end-to-end production RAG system