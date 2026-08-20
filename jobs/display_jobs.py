def display_jobs(jobs: list, limit=None, title=None):
    job_list = [{
        "company_name": job["company_name"],
        "title": job["title"],
        "location": job["location"] or "Not specified",
        "job_types": job["job_types"]
    } for job in jobs[:limit]]

    print(f"----- {title} -----")

    for job in job_list:
        print(f"Company: {job["company_name"]}")
        print(f"Title: {job["title"]}")
        print(f"Location: {job["location"]}")
        print(
            f"Type: {job["job_types"][0] if job["job_types"] else "Not specified"}")
        print("-" * 50)
