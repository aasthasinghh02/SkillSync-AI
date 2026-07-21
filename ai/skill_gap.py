from ai.base_ai import run_prompt
from ai.prompts import SKILL_GAP_PROMPT


def analyze_skill_gap(resume_text, job_description):

    prompt = SKILL_GAP_PROMPT.format(
        resume=resume_text,
        job_description=job_description
    )

    return run_prompt(prompt)