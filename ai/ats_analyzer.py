from ai.base_ai import run_prompt
from ai.prompts import ATS_ANALYZER_PROMPT


def analyze_ats(resume_text, job_description):

    prompt = ATS_ANALYZER_PROMPT.format(
        resume=resume_text,
        job_description=job_description
    )

    return run_prompt(prompt)