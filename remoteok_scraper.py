import requests
from parser.validator import validate_job  # import your validator

REMOTEOK_URL = "https://remoteok.com/api"

def fetch_remoteok_jobs(filtered=True):
    """
    Fetch remote jobs from RemoteOK API.
    If filtered=True, only return jobs matching EA/admin + English + remote criteria.
    """
    response = requests.get(REMOTEOK_URL, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        print(f"Failed to fetch jobs: {response.status_code}")
        return []
    
    data = response.json()
    jobs = []

    for item in data:
        if "position" not in item:
            continue

        job = {
            "title": item.get("position"),
            "company": item.get("company"),
            "location": item.get("location", "Remote"),
            "description": item.get("description", ""),
            "url": f"https://remoteok.com/{item.get('id')}"
        }

        if filtered and not validate_job(job):
            continue  # skip jobs that don't match criteria

        jobs.append(job)
    
    return jobs

# Quick test
if __name__ == "__main__":
    jobs = fetch_remoteok_jobs()
    print(f"Found {len(jobs)} filtered jobs")
    for job in jobs[:5]:
        print(job)

