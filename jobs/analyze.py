import os
import openai
import time
from openai import OpenAI
from pydantic import BaseModel
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from jobs.constants import TECH_TAGS
from jobs.exceptions import handle_openai_error
from jobs.normalization import normalize_skills
from jobs.cache import load_cache, generate_cache_key, save_cache

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class Skill(BaseModel):
    skills: list[str]


def filter_by_city(jobs_list: list, location: str) -> list:
    return list(filter(lambda job: location in job["location"], jobs_list))


def filter_by_it_category(jobs_list: list) -> list:
    return list(filter(lambda job: any(tag in TECH_TAGS for tag in job["tags"]), jobs_list))


def extract_skills(description: str, cache: dict) -> list[str]:
    cache_key = generate_cache_key(description)

    if cache_key in cache:
        return cache[cache_key]

    for attempt in range(3):
        try:
            response = client.responses.parse(model="gpt-5.6-luna", input=f"""
                    Extract technical skills from the job description, regardless of the language of the job description.
        
                    Include only specific technologies, tools, programming languages, frameworks, libraries, databases, cloud platforms, or DevOps tools.
        
                    Do not include broad technical areas or concepts, human languages, soft skills,
                    job responsibilities, job titles, or general business skills.
        
                    Description:
                    {description}
                    """, text_format=Skill,)

        except openai.APIError as e:
            if isinstance(e, openai.APITimeoutError) or isinstance(e, openai.APIConnectionError) or isinstance(e, openai.InternalServerError):
                if attempt < 2:
                    time.sleep(1)
                continue
            else:
                return handle_openai_error(e)

        else:
            return response.output_parsed.skills
    return []


def extract_skills_from_jobs(jobs_list: list) -> list[list[str]]:
    cache = load_cache()
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(lambda job: normalize_skills(extract_skills(
            job["description"], cache)), jobs_list)

    results = list(results)
    for job, skills in zip(jobs_list, results):
        cache_key = generate_cache_key(job["description"])
        cache[cache_key] = skills

    save_cache(cache)

    return results


def count_skills(skills_by_job: list[list[str]]) -> Counter:
    skill_counts = Counter()

    for skills in skills_by_job:
        skill_counts.update(skills)
    return skill_counts
