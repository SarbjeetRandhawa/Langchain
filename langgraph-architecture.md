# LangGraph multi-agent architecture

## 1. Full request lifecycle

```mermaid
flowchart TD
    A[User] --> B[API / Frontend Layer]
    B --> C[Authentication]
    B --> D[Rate Limiting]
    C --> E[Input Validation<br/>files, prompt injection, permissions]
    D --> E
    E --> F[Load Conversation State<br/>Checkpoint + Chat History + Memory]
    F --> G[Retrieve Long-Term Memory<br/>Vector Memory / Entity Memory / User Profile]
    G --> H([START - LangGraph])
    H --> I[Planner / Supervisor Node]

    I --> J[Research Agent<br/>ReAct Loop]
    I --> K[Coding Agent<br/>ReAct Loop]
    I --> L[Finance Agent<br/>ReAct Loop]

    J --> M{Need Tool?}
    K --> N{Need Tool?}
    L --> O{Need Tool?}

    M -- Yes --> P[Tool Execution Node]
    M -- No --> Q[Continue<br/>LLM reasons over observation]
    N -- Yes --> P
    N -- No --> Q
    O -- Yes --> P
    O -- No --> Q

    P --> R[Retriever / SQL / API / MCP /<br/>Calculator / GitHub / Python /<br/>Email / Weather / Custom Tools]
    R --> S[Receive Observation]
    S --> T[Continue ReAct Reasoning]
    T --> U[Update Shared State]
    Q --> U

    U --> V{More Work Required?}
    V -- Yes --> W[Route to Another Agent]
    W --> I
    V -- No --> X[Produce Result]

    X --> Y[Guardrails<br/>Validate Output]
    Y --> Z{Safe Output?}
    Z -- Yes --> AA{Human Approval Needed?}
    Z -- No --> AB[Retry / Reject]
    AB --> AC[Failure Recovery]

    AA -- Yes --> AD[Pause Graph<br/>Await Human Input]
    AA -- No --> AE[Continue Execution]
    AD --> AF[Save Checkpoint / Memory]
    AE --> AF

    AF --> AG[Logging + Metrics + Tracing]
    AG --> AH([END NODE])
    AH --> AI[Final Response]
```

## 2. Agent reasoning loop (ReAct)

```mermaid
flowchart TD
    A[Current State] --> B[Read User Goal]
    B --> C[Multi-Step Reasoning]
    C --> D{Need External Tool?}
    D -- No --> E[Continue Reasoning]
    D -- Yes --> F[Tool Call]
    F --> G[Observation]
    G --> C
    E --> H{Enough Information?}
    G --> H
    H -- No --> C
    H -- Yes --> I[Update Shared State]
    I --> J[Return Control]
```

## 3. Shared state schema

```python
State = {
    # Conversation
    "messages": [],

    # Planner
    "current_task": "",
    "plan": [],

    # Memory
    "chat_history": [],
    "summary": "",
    "entities": {},
    "long_term_memory": [],

    # Retrieval
    "query": "",
    "retrieved_chunks": [],
    "reranked_chunks": [],

    # Tooling
    "tool_calls": [],
    "tool_results": [],

    # Agents
    "active_agent": "",
    "next_agent": "",

    # Output
    "draft_answer": "",
    "final_answer": "",

    # Errors
    "retry_count": 0,
    "error": None,

    # Human Approval
    "approval_required": False,
    "approval_status": None,

    # Metadata
    "session_id": "",
    "user_id": "",
    "cost": 0,
    "token_usage": 0,
}
```

## 4. Planner / supervisor

```mermaid
flowchart TD
    A[User Request] --> B[Understand Intent]
    B --> C[Break Into Tasks]
    C --> D[Choose Agent]
    D --> E[Execute]
    E --> F{Need More Work?}
    F -- Yes --> G[Next Agent]
    G --> E
    F -- No --> H[Finish]
```

## 5. Failure recovery graph

```mermaid
flowchart TD
    A[Execute Node] --> B{Success?}
    B -- Yes --> C[Continue]
    B -- No --> D{Retry?}
    D -- Yes --> E[Retry Node]
    E --> A
    D -- No --> F{Fallback Available?}
    F -- Yes --> G[Fallback Tool]
    F -- No --> H[Human Approval]
    H --> I[Abort or Continue]
```

## 6. Human-in-the-loop (e.g. SQL execution)

```mermaid
flowchart TD
    A[Generate SQL] --> B{Dangerous?}
    B -- No --> C[Execute]
    B -- Yes --> D[Pause Graph]
    D --> E[Human Reviews SQL]
    E --> F{Approve or Reject}
    F -- Approve --> C
    F -- Reject --> G[Stop]
```
