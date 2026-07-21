from ai.client import generate_response
from utils.json_utils import extract_json


def run_prompt(prompt: str):

    response = generate_response(prompt)

    ai_output = response["response"]

    return extract_json(ai_output)