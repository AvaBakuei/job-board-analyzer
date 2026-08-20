from jobs.data import data_load
from jobs.analyze import filter_by_city
from jobs.display_jobs import display_jobs


def main():
    jobs = data_load()
    display_jobs(jobs, limit=8, title="List of Jobs")

    jobs_city = filter_by_city(jobs, 'Frankfurt')
    display_jobs(jobs_city, title="Filter by City")


if __name__ == "__main__":
    main()
