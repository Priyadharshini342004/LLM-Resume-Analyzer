SKILLS_DB = [
    "python", "machine learning", "deep learning",
    "nlp", "sql", "react", "javascript", "data analysis"
]

def extract_skills(text):
    found_skills = []
    text = text.lower()
    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)
    return found_skills
