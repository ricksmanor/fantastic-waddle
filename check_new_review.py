
import requests
import json
import os
from datetime import datetime
from github import Github  # pip install PyGithub

# === CONFIG ===
TRUSTPILOT_URL = "https://uk.trustpilot.com/review/ukstoragecompany.co.uk"
LAST_REVIEW_FILE = "last_review.txt"
GITHUB_TOKEN = "YOUR_PERSONAL_ACCESS_TOKEN"
REPO_NAME = "your-username/your-repo"
WORKFLOW_FILE = "update_excel.yml"  # GitHub Action workflow file

# === FUNCTION TO GET LATEST REVIEW DATE ===
def get_latest_review_date():
    response = requests.get(TRUSTPILOT_URL)
    # This depends on how you parse Trustpilot HTML or API
    # For demo, assume JSON endpoint returns list of reviews
    data = response.json()
    latest_review = data["data"][0]  # first review is newest
    return latest_review["date"]  # ISO format expected

# === READ LAST STORED REVIEW ===
if os.path.exists(LAST_REVIEW_FILE):
    with open(LAST_REVIEW_FILE, "r") as f:
        last_date = f.read().strip()
else:
    last_date = ""

latest_date = get_latest_review_date()

if latest_date != last_date:
    print("New review detected! Triggering GitHub Action...")

    # Trigger GitHub Action
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    workflow = repo.get_workflow(WORKFLOW_FILE)
    workflow.create_dispatch("main")  # branch name

    # Update last_review.txt
    with open(LAST_REVIEW_FILE, "w") as f:
        f.write(latest_date)
else:
    print("No new review.")
