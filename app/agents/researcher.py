from app.tools.file_utils import clone_repo
from app.core.logger import log_event
import os


def researcher_agent(state):

    repo_name = state["issue"]["repo"]   # "owner/repo"
    repo_url = f"https://github.com/{repo_name}.git"
    local_path = f"/tmp/{repo_name.replace('/', '_')}"

    try:
        # 🔥 Clone repo (safe version handles overwrite)
        clone_repo(repo_url, local_path)

        # 🔥 Store repo path
        state["context"]["repo_path"] = local_path

        # 🔥 Basic file discovery (initial version)
        files = []

        for root, _, filenames in os.walk(local_path):
            for file in filenames:
                if file.endswith(".py"):   # only python files for now
                    rel_path = os.path.relpath(os.path.join(root, file), local_path)
                    files.append(rel_path)

        # fallback if no python files
        if not files:
            files = ["README.md"]

        state["context"]["relevant_files"] = files[:5]  # limit for now

        log_event({
            "agent": "researcher",
            "repo": repo_name,
            "files_found": len(files),
            "sample_files": state["context"]["relevant_files"]
        })

        print(f"🔍 Found {len(files)} files")

    except Exception as e:
        print("❌ Repo cloning failed:", str(e))

        state["status"] = "failed"

        log_event({
            "agent": "researcher",
            "error": str(e)
        })

        return state

    return state