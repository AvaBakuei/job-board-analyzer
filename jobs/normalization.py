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
    for skill in skills:
        if skill in mapping_skills:
            normal_skills.append(mapping_skills[skill])
        else:
            normal_skills.append(skill)
    return normal_skills
