RAY Case Study Pipeline
Project Overview

This project automates the sourcing, filtering, and outreach process for remote Executive Assistant (EA) and administrative job postings. It:

Scrapes RemoteOK for remote job listings.

Validates roles to ensure they are remote, require English, and match EA/admin positions.

Generates personalized outreach messages using OpenAI’s GPT-3.5 model.

Writes results to Google Sheets for easy tracking.

The pipeline is modular and structured for easy extension to other job boards in the future.

Folder Structure
ray_case_study/
│
├── scraper/           # Scrapers for different job boards
│   └── remoteok_scraper.py
│
├── parser/            # Job validation logic
│   └── validator.py
│
├── llm/               # Outreach message generator
│   └── generator.py
│
├── sheets/            # Google Sheets integration
│   └── sheets_writer.py
│
├── utils/             # Configs, filters, helper functions
│
├── main.py            # Entry point for the pipeline
├── requirements.txt   # Python dependencies
└── README.md

Setup Instructions

Clone the repository

git clone https://github.com/<your-username>/ray_case_study.git
cd ray_case_study


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Set up environment variables

Create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key
GOOGLE_SERVICE_ACCOUNT_JSON=service_account.json


⚠️ Make sure .env and service_account.json are added to .gitignore to avoid pushing secrets.

Usage

Run the pipeline:

python main.py


The pipeline will fetch remote EA/admin jobs from RemoteOK.

Jobs are filtered using the validation module.

Outreach messages are generated via OpenAI.

Results are appended to the specified Google Sheet.

Extending the Pipeline

Add new scrapers in scraper/ for other job boards (SimplyHired, Indeed, etc.).

Customize validation rules in parser/validator.py.

Adjust message tone or template in llm/generator.py.

Change output sheet or add multiple sheets in sheets/sheets_writer.py.

Dependencies

requests – for HTTP requests

beautifulsoup4 – HTML parsing (if you extend to other boards)

playwright – optional for dynamic websites

python-dotenv – loading environment variables

openai – OpenAI API integration

gspread / oauth2client – Google Sheets API

pandas – optional for data handling

schedule – optional for recurring pipeline runs

Author

Sharon Wainaina – Cloud/DevOps engineer & automation enthusiast
