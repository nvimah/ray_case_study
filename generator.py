import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
Write a short, professional outreach message to the hiring manager for this job:

Job Title: {title}
Company: {company}
Job Description: {description}

Tone: warm, concise, proactive.
"""

def generate_message(job):
    """
    Generates a personalized outreach message for a given job.
    `job` should be a dict with keys: title, company, description
    """
    prompt = PROMPT_TEMPLATE.format(**job)

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=180
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating message: {e}")
        return ""

