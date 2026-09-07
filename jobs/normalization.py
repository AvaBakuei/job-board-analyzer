mapping_skills = {
    "ReactJS": "React",
    "React.js": "React",
    "AWS Cloud": "AWS",
    "Amazon Web Services": "AWS",
    "Amazon Web Services (AWS)": "AWS",
    "Postgres": "PostgreSQL",
}


def normalize_skills(skills: list[str]):
    normal_skills = []
    unique_skills = []

    for skill in skills:
        for key, value in mapping_skills.items():
            if key.casefold() == skill.casefold():
                normal_skills.append(value)
                break
        else:
            normal_skills.append(skill)

    for skill in normal_skills:
        if not any(skill.casefold() == existing.casefold() for existing in unique_skills):
            unique_skills.append(skill)

    return unique_skills
