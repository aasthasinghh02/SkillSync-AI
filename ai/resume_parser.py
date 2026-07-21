from ai.base_ai import run_prompt
from ai.prompts import RESUME_PARSER_PROMPT


def parse_resume(resume_text):

    prompt = RESUME_PARSER_PROMPT.format(
        resume=resume_text
    )

    return run_prompt(prompt)