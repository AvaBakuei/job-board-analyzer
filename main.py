from jobs.data import data_load
from jobs.analyze import filter_by_city, filter_by_it_category, count_skills, extract_skills_from_jobs
from jobs.display_jobs import display_jobs


def main():
    jobs = data_load()

    display_jobs(jobs, limit=8, title="List of Jobs")

    jobs_city = filter_by_city(jobs, "Frankfurt")
    display_jobs(jobs_city, title="Filter by City")

    tech_category = filter_by_it_category(jobs)
    display_jobs(tech_category, title="Filter by IT Category", show_tags=True)

    skills_by_job = extract_skills_from_jobs(tech_category)

    skill_counts = count_skills(skills_by_job)

    print(skill_counts.most_common())


if __name__ == "__main__":
    main()
