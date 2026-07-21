import json
import re


def extract_json(text):
    """
    Extract JSON from an LLM response.
    """

    # Remove Markdown code fences
    text = re.sub(r"```json", "", text)
    text = re.sub(r"```", "", text)

    # Find the first JSON object
    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON found in AI response.")

    json_text = text[start:end + 1]

    return json.loads(json_text)