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
- <details>
  <summary>✅ Phase 5 - LCEL ⭐⭐⭐⭐⭐</summary>
  <br>
  &nbsp;&nbsp;&nbsp; &bull; ✅ What is LCEL?<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 2 → RunnableSequence (the `|` operator)<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 3 → RunnableLambda<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 4 → RunnablePassthrough<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 5 → RunnableParallel<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 6 → RunnableAssign<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 7 → RunnableBranch<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 8 → LCEL Execution (invoke, batch, stream)<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 9 → Building Complete AI Pipelines<br>
  &nbsp;&nbsp;&nbsp; &bull; Lesson 10 → Production Patterns<br>
  <br>
  &nbsp;&nbsp;&nbsp; <b>Theory:</b><br>
  &nbsp;&nbsp;&nbsp; &bull; <b>Execution Methods:</b> LCEL runnables support various execution methods. `invoke()` is used for single inputs, returning the final output. `batch()` processes a list of inputs concurrently, optimizing for speed. `stream()` yields chunks of the output as soon as they are available, crucial for building responsive UIs.<br>
  &nbsp;&nbsp;&nbsp; &bull; <b>Building Pipelines:</b> Combining different LCEL components (prompts, models, parsers, runnables) allows you to build complex AI pipelines. You can seamlessly chain multiple steps, routing inputs based on conditions (RunnableBranch), or running tasks concurrently (RunnableParallel).<br>
  &nbsp;&nbsp;&nbsp; &bull; <b>Production Patterns:</b> In production, LCEL simplifies adding fallback models, retry logic (using RetryOutputParser), and observability. Because of its standard interface, integrating LangSmith for tracing and debugging comes almost for free.
  </details>
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