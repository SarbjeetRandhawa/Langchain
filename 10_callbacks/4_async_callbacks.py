"""
Phase 15: Callbacks - Async Callbacks

This script demonstrates how to handle callbacks in an asynchronous execution
environment. This is crucial for high-performance applications like web servers 
(e.g., FastAPI) where you don't want to block the event loop.
"""

from dotenv import load_dotenv
import asyncio
from typing import Any, Dict, List
from langchain_core.callbacks import AsyncCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()

# 1. Define an Async Callback Handler
# We inherit from AsyncCallbackHandler instead of BaseCallbackHandler
class MyAsyncHandler(AsyncCallbackHandler):
    async def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running (Async)."""
        print("\\n[ASYNC HANDLER] LLM Started!")
        # Simulate some async work (e.g., writing to a database)
        await asyncio.sleep(0.1)

    async def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token (Async)."""
        print(f"{token}", end="", flush=True)

    async def on_llm_end(self, response: Any, **kwargs: Any) -> None:
        """Run when LLM ends running (Async)."""
        print("\\n\\n[ASYNC HANDLER] LLM Finished!")

async def main():
    # 2. Initialize LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)
    handler = MyAsyncHandler()
    
    print("Starting async LLM invocation...")
    
    # 3. Use the ainvoke method for asynchronous execution
    await llm.ainvoke(
        [HumanMessage(content="Write a very short haiku about asynchronous programming.")],
        config={"callbacks": [handler]}
    )

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main())
