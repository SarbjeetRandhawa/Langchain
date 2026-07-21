"""
Phase 16: LangSmith & Production - Evaluating Runs

This script demonstrates how to evaluate an LLM app using LangSmith.
Evaluations are critical for measuring performance over time and guarding against regressions.
"""

from dotenv import load_dotenv
import os
from langsmith import Client
from langsmith.evaluation import evaluate, LangChainStringEvaluator
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# We need the LangSmith Client
client = Client()

# 1. Define the app we want to evaluate
def predict_sentiment(inputs: dict) -> dict:
    """A simple function representing our application."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = PromptTemplate.from_template("Classify the sentiment of this text as POSITIVE or NEGATIVE: {text}")
    chain = prompt | llm
    
    # We must return a dictionary for the evaluator
    response = chain.invoke(inputs)
    return {"output": response.content}

if __name__ == "__main__":
    # Ensure LangSmith API key is set
    if not os.environ.get("LANGCHAIN_API_KEY"):
        print("Error: LANGCHAIN_API_KEY is not set.")
        exit(1)
        
    dataset_name = "Sentiment-Analysis-Test-Dataset"
    
    # 2. Create a dataset programmatically (if it doesn't exist)
    if not client.has_dataset(dataset_name=dataset_name):
        print(f"Creating dataset '{dataset_name}'...")
        dataset = client.create_dataset(
            dataset_name=dataset_name,
            description="A dataset for evaluating sentiment analysis",
        )
        
        # Add examples to the dataset
        examples = [
            ("I absolutely love this new feature!", "POSITIVE"),
            ("This update completely broke my workflow.", "NEGATIVE"),
            ("The food was okay, but the service was terrible.", "NEGATIVE"),
            ("Wow, the speed improvements are incredible.", "POSITIVE")
        ]
        
        for input_text, expected_output in examples:
            client.create_example(
                inputs={"text": input_text},
                outputs={"output": expected_output},
                dataset_id=dataset.id,
            )
        print("Dataset created successfully.")
    else:
        print(f"Dataset '{dataset_name}' already exists.")

    # 3. Define the Evaluator
    # This built-in evaluator uses an LLM to check if the prediction matches the expected output
    exact_match_evaluator = LangChainStringEvaluator("exact_match")
    
    # 4. Run the Evaluation
    print("Running evaluation on the dataset (this will make LLM calls)...")
    
    experiment_results = evaluate(
        predict_sentiment,
        data=dataset_name,
        evaluators=[exact_match_evaluator],
        experiment_prefix="sentiment-eval-",
        metadata={"version": "1.0"},
    )
    
    print("\\nEvaluation complete!")
    print("Check your LangSmith dashboard to see the detailed results.")
