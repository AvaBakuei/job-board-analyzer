def display_jobs(jobs: list, limit=None, title=None, show_tags=False):

    job_list = [
        {
            "company_name": job["company_name"],
            "title": job["title"],
            "location": job.get("location") or "Not specified",
            "job_types": job.get("job_types") or [],
            "tags": job.get("tags") or [],
        }
        for job in jobs[:limit]
    ]

    print(f"----- {title} -----")

    for job in job_list:
        print(f"Company: {job['company_name']}")
        print(f"Title: {job['title']}")
        print(f"Location: {job['location']}")

        job_types = job.get("job_types") or []

        if isinstance(job_types, list) and job_types:
            job_type = job_types[0]
        elif isinstance(job_types, dict) and job_types:
            job_type = next(iter(job_types.values()))
        else:
            job_type = "Not specified"

        print(f"Type: {job_type}")

        if show_tags:
            print(f"Tags: {job['tags']}")

        print("-" * 50)
