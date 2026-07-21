import json
import requests

from config import (
    OLLAMA_HOST,
    OLLAMA_MODEL,
)


def generate_response(prompt: str) -> dict:
    """
    Send a prompt to Ollama and return JSON.
    """

    url = f"{OLLAMA_HOST}/api/generate"

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            url,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result

    except requests.exceptions.RequestException as e:

        raise Exception(
            f"Ollama Error: {e}"
        )