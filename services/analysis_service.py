from ai.resume_parser import parse_resume
from ai.ats_analyzer import analyze_ats
from ai.skill_gap import analyze_skill_gap
from ai.roadmap_generator import generate_roadmap


def analyze_resume_pipeline(resume_text, job_description):

    parsed_resume = parse_resume(resume_text)

    ats = analyze_ats(
        resume_text,
        job_description
    )

    skill_gap = analyze_skill_gap(
        resume_text,
        job_description
    )

    roadmap = generate_roadmap(
        skill_gap["critical_skills"]
    )

    return {
        "resume": parsed_resume,
        "ats": ats,
        "skill_gap": skill_gap,
        "roadmap": roadmap
    }