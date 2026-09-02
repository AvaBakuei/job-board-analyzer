import os
import json
import openai
from openai import OpenAI
from json.decoder import JSONDecodeError
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
from jobs.constants import TECH_TAGS
from jobs.exceptions import handle_openai_error

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def filter_by_city(jobs_list: list, location: str) -> list:
    return list(filter(lambda job: location in job["location"], jobs_list))


def filter_by_it_category(jobs_list: list) -> list:
    return list(filter(lambda job: any(tag in TECH_TAGS for tag in job["tags"]), jobs_list))


def extract_skills(description: str) -> list[str]:
    try:
        response = client.responses.create(model="gpt-5.6-luna", input=f"""
            Extract technical skills from the job description, regardless of the language.

            Return a JSON object with this format:
            {{"skills": ["Python", "React", "Docker"]}}

            Description:
            {description}
            """)

    except openai.APIError as e:
        return handle_openai_error(e)
    else:
        try:
            return json.loads(response.output_text)["skills"]
        except JSONDecodeError as e:
            print(f"Failed to decode OpenAI response as JSON: {e}")
            return []


def extract_skills_from_jobs(jobs_list: list) -> list[list[str]]:
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(lambda job: extract_skills(
            job["description"]), jobs_list)

    return list(results)


def count_skills(skills_by_job: list[list[str]]) -> Counter:
    skill_counts = Counter()

    for skills in skills_by_job:
        skill_counts.update(skills)
    return skill_counts
