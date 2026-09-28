import json
import sys
import urllib.request

sys.stdout.reconfigure(encoding="utf-8")

url = "https://remotive.com/api/remote-jobs?category=software-dev"
request = urllib.request.Request(url, headers={"User-Agent": "alert-dashboard-learning/1.0"})

with urllib.request.urlopen(request) as response:
    data = json.loads(response.read())

jobs = data["jobs"]

for job in jobs[:10]:
    print(job["title"], "|", job["company_name"], "|", job["candidate_required_location"])

print()
print("Total jobs returned:", len(jobs))
print("Jobs from Remotive: https://remotive.com")
