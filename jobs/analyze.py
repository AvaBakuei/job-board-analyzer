def filter_by_city(jobs_list: list, location: str) -> list:
    return list(filter(lambda job: location in job["location"], jobs_list))
