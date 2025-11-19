import re

def is_remote(job):
    keywords = ["remote", "work from home", "anywhere"]
    text = f"{job.get('location','')} {job.get('description','')}"
    return any(re.search(rf"\b{k}\b", text, re.IGNORECASE) for k in keywords)

def requires_english(job):
    keywords = ["english", "fluent english", "excellent communication"]
    text = job.get("description","")
    return any(re.search(rf"\b{k}\b", text, re.IGNORECASE) for k in keywords)

def is_ea_or_admin(job):
    keywords = [
        "executive assistant", 
        "admin assistant",
        "administrative assistant",
        "ea",
        "personal assistant"
    ]
    text = f"{job.get('title','')} {job.get('description','')}"
    return any(re.search(rf"\b{k}\b", text, re.IGNORECASE) for k in keywords)

def validate_job(job):
    """
    Returns True if the job is remote, requires English, and is an EA/admin role.
    """
    return is_remote(job) and requires_english(job) and is_ea_or_admin(job)

