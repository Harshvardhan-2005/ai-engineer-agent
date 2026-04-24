import requests
import os

# 🔐 Load token from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

if not GITHUB_TOKEN:
    raise ValueError("❌ GITHUB_TOKEN not set in environment variables")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


# 🔍 Get issue details
def get_issue(owner, repo, issue_number):

    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    res = requests.get(url, headers=HEADERS)

    if res.status_code == 200:
        print("✅ Issue fetched successfully")
        return res.json()
    else:
        print("❌ Failed to fetch issue")
        print("Status:", res.status_code)
        print("Response:", res.text)
        return None


# 🌿 Create new branch from base branch
def create_branch(owner, repo, base_branch, new_branch):

    # get base branch SHA
    ref_url = f"https://api.github.com/repos/{owner}/{repo}/git/ref/heads/{base_branch}"
    ref_res = requests.get(ref_url, headers=HEADERS)

    if ref_res.status_code != 200:
        print("❌ Failed to fetch base branch")
        print("Response:", ref_res.text)
        return None

    sha = ref_res.json()["object"]["sha"]

    # create new branch
    url = f"https://api.github.com/repos/{owner}/{repo}/git/refs"

    data = {
        "ref": f"refs/heads/{new_branch}",
        "sha": sha
    }

    res = requests.post(url, headers=HEADERS, json=data)

    if res.status_code == 201:
        print("✅ Branch created successfully")
        return res.json()
    else:
        print("❌ Failed to create branch")
        print("Status:", res.status_code)
        print("Response:", res.text)
        return None


# 🚀 Create Pull Request
def create_pr(owner, repo, branch, title, body):

    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"

    data = {
        "title": title,
        "body": body,
        "head": branch,
        "base": "main"
    }

    res = requests.post(url, headers=HEADERS, json=data)

    if res.status_code == 201:
        pr_data = res.json()
        print("✅ Pull Request created successfully")
        print("🔗 PR URL:", pr_data.get("html_url"))
        return pr_data
    else:
        print("❌ Failed to create PR")
        print("Status:", res.status_code)
        print("Response:", res.text)
        return None