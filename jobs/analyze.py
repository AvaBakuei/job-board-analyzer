import spacy
from spacy.matcher import PhraseMatcher
from jobs.constants import TECH_TAGS, TECH_SKILLS
from collections import Counter

nlp = spacy.load("en_core_web_lg")


def filter_by_city(jobs_list: list, location: str) -> list:
    return list(filter(lambda job: location in job["location"], jobs_list))


def filter_by_it_category(jobs_list: list) -> list:
    return list(filter(lambda job: any(tag in TECH_TAGS for tag in job["tags"]), jobs_list))


def extract_skills(description: str) -> list[str]:
    description = description.lower()

    return [
        skill
        for skill in TECH_SKILLS
        if skill in description
    ]


def extract_skills_from_jobs(jobs_list: list) -> list:
    all_skills = []

    for job in jobs_list:
        skills = extract_skills(job["description"])
        all_skills.extend(skills)

    return list(set(all_skills))


def count_skills(jobs_list: list) -> Counter:
    skill_counts = Counter()
    for job in jobs_list:
        skills = extract_skills(job["description"])
        skill_counts.update(skills)
    return skill_counts
