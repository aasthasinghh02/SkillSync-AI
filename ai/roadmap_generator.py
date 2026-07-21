from ai.base_ai import run_prompt
from ai.prompts import ROADMAP_PROMPT


def generate_roadmap(skills):

    prompt = ROADMAP_PROMPT.format(
        skills=", ".join(skills)
    )

    return run_prompt(prompt)