import json
from ollama import chat
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from jobs.constants import TECH_TAGS


def filter_by_city(jobs_list: list, location: str) -> list:
    return list(filter(lambda job: location in job["location"], jobs_list))


def filter_by_it_category(jobs_list: list) -> list:
    return list(filter(lambda job: any(tag in TECH_TAGS for tag in job["tags"]), jobs_list))


def extract_skills(description: str) -> list[str]:
    response = chat(model="qwen2.5:7b-instruct", format="json", messages=[{
        "role": "user",
        "content": f"""
            Extract technical skills from the job description, regardless of the language.

            Return a JSON object with this format:
            {{"skills": ["Python", "React", "Docker"]}}

            Description:
            {description}
            """
    }])

    return json.loads(response.message.content)["skills"]


def extract_skills_from_jobs(jobs_list: list) -> list:
    all_skills = []

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(lambda job: extract_skills(
            job["description"]), jobs_list)

    for skill in results:
        all_skills.extend(skill)

    return list(set(all_skills))


def count_skills(jobs_list: list) -> Counter:
    skill_counts = Counter()
    for job in jobs_list:
        skills = extract_skills(job["description"])
        skill_counts.update(skills)
    return skill_counts
