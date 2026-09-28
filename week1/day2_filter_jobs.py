import json
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

url = "https://remotive.com/api/remote-jobs?category=software-dev"
request = urllib.request.Request(url, headers={"User-Agent": "alert-dashboard-learning/1.0"})

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read())

jobs = data["jobs"]

latam_words = ["latam", "latin america", "americas", "mexico", "argentina", "brazil", "colombia", "chile", "peru"]

matches = []

for job in jobs:
    location = job["candidate_required_location"].lower()
    for word in latam_words:
        if word in location:
            matches.append(job)
            break

for job in matches:
    print(job["title"], "|", job["company_name"], "|", job["candidate_required_location"])

print()
print(len(matches), "of", len(jobs), "jobs are open to LATAM")
print("Jobs from Remotive: https://remotive.com")
