from scraper.remoteok_scraper import fetch_remoteok_jobs
from parser.validator import validate_job
from llm.generator import generate_message
from sheets.sheets_writer import get_sheet, append_job

def run_pipeline():
    print("Fetching jobs...")
    jobs = fetch_remoteok_jobs(filtered=True)

    print(f"Valid postings: {len(jobs)}")

    sheet = get_sheet("RAY Job Dashboard")

    for job in jobs:
        try:
            job["message"] = generate_message(job)
        except Exception as e:
            print(f"LLM generation failed for {job['title']}: {e}")
            job["message"] = ""
        try:
            append_job(sheet, job)
        except Exception as e:
            print(f"Failed to append {job['title']} to sheet: {e}")
    
    print("Pipeline complete.")

if __name__ == "__main__":
    run_pipeline()

