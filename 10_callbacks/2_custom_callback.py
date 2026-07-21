"""
Phase 15: Callbacks - Custom Callback Handlers

This script demonstrates how to create a custom callback handler by inheriting
from BaseCallbackHandler. This allows you to hook into specific events in the
lifecycle of an LLM, Chain, or Tool.
"""

from dotenv import load_dotenv
from typing import Any, Dict, List
from langchain_core.callbacks import BaseCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.outputs import LLMResult

load_dotenv()

# 1. Define the Custom Callback Handler
class MyCustomHandler(BaseCallbackHandler):
    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> None:
        """Run when LLM starts running."""
        print(f"[CUSTOM HANDLER] LLM is starting. Processing {len(prompts)} prompt(s).")
        # You can inspect the prompt here
        print(f"[CUSTOM HANDLER] Prompt snippet: {prompts[0][:50]}...")

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        """Run on new LLM token. Only available when streaming is enabled."""
        # Print tokens as they arrive, but with a special prefix
        print(f"[{token}]", end="", flush=True)

    def on_llm_end(self, response: LLMResult, **kwargs: Any) -> None:
        """Run when LLM ends running."""
        print(f"\\n\\n[CUSTOM HANDLER] LLM execution finished.")
        print(f"[CUSTOM HANDLER] Token usage: {response.llm_output.get('token_usage', 'N/A')}")

    def on_llm_error(self, error: Exception, **kwargs: Any) -> None:
        """Run when LLM errors."""
        print(f"\\n[CUSTOM HANDLER] LLM encountered an error: {error}")

if __name__ == "__main__":
    # Initialize the LLM with streaming enabled so we can see the tokens
    llm = ChatOpenAI(model="gpt-3.5-turbo", streaming=True)
    
    handler = MyCustomHandler()
    
    print("Sending request to LLM...")
    
    # Pass the callback handler in the config
    llm.invoke(
        [HumanMessage(content="Explain the concept of 'callbacks' in software engineering in 2 sentences.")],
        config={"callbacks": [handler]}
    )
