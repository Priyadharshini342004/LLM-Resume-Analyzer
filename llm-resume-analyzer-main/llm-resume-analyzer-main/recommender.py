import json

def recommend_jobs(skills):
    with open("data/job_roles.json") as f:
        jobs = json.load(f)

    recommendations = []

    for job, job_skills in jobs.items():
        match = set(skills).intersection(set(job_skills))
        if len(match) >= 2:
            recommendations.append(job)

    return recommendations
