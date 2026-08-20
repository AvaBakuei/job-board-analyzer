from jobs.data import data_load
from jobs.analyze import extract_skills_from_jobs, filter_by_city, filter_by_it_category, count_skills
from jobs.display_jobs import display_jobs


def main():
    jobs = data_load()

    display_jobs(jobs, limit=8, title="List of Jobs")

    jobs_city = filter_by_city(jobs, "Frankfurt")
    display_jobs(jobs_city, title="Filter by City")

    tech_category = filter_by_it_category(jobs)
    display_jobs(tech_category, title="Filter by IT Category", show_tags=True)
    print(len(tech_category))

    skills = extract_skills_from_jobs(tech_category)

    skill_counts = count_skills(tech_category)

    print(skill_counts.most_common())
    print("skills:   ", skills)


if __name__ == "__main__":
    main()
