import os
from pathlib import Path
from dotenv import load_dotenv


def load_config(env_path: str | None = None) -> dict:
    """Load environment variables and return a config dict."""
    root = Path(__file__).resolve().parents[2]
    dotenv_path = Path(env_path) if env_path else root / ".env"
    load_dotenv(dotenv_path)

    return {
        "openai_api_key": os.environ.get("OPENAI_API_KEY", ""),
        "cohere_api_key": os.environ.get("COHERE_API_KEY", ""),
        "anthropic_api_key": os.environ.get("ANTHROPIC_API_KEY", ""),
        "pinecone_api_key": os.environ.get("PINECONE_API_KEY", ""),
        "pinecone_environment": os.environ.get("PINECONE_ENVIRONMENT", ""),
        "langchain_tracing": os.environ.get("LANGCHAIN_TRACING_V2", "false"),
        "langchain_api_key": os.environ.get("LANGCHAIN_API_KEY", ""),
        "langchain_project": os.environ.get(
            "LANGCHAIN_PROJECT", "rag-architectures-and-evaluation"
        ),
    }
