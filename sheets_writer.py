import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet(sheet_name):
    """
    Connects to Google Sheets using a service account.
    Returns the first worksheet.
    """
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds_file = os.getenv("GOOGLE_SERVICE_ACCOUNT_JSON", "service_account.json")
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1

def append_job(sheet, job):
    """
    Appends a job dictionary as a row in the Google Sheet.
    """
    row = [
        job.get("url", ""),
        job.get("title", ""),
        job.get("company", ""),
        job.get("location", ""),
        job.get("description", "")[:500],  # truncate long descriptions
        job.get("message", "")
    ]
    sheet.append_row(row)

