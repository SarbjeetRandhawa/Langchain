# Langchain

- <details>
  <summary>✅ Phase 1 - Why LangChain Exists</summary>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b> LangChain provides a standard interface for building applications powered by LLMs. Before LangChain, developers had to write custom boilerplate code to connect to different LLM providers, manage complex prompts, parse outputs manually, and handle context windows. LangChain abstracts away all of this complexity into a unified framework. It makes it incredibly simple to build robust, production-ready applications like RAG (Retrieval-Augmented Generation) systems, dynamic agents, and complex chatbots by providing built-in orchestration, prompt management, memory, and tool-calling capabilities out of the box.<br>
  </details>
- <details>
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
- <details>
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
- <details>
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
- ➡️ Phase 5 - LCEL ⭐⭐⭐⭐⭐
- ➡️ Phase 6 - Chains
- ➡️ Phase 7 - Document Loaders
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