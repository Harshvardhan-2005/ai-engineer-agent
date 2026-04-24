import subprocess
import os
import shutil


def clone_repo(repo_url, path):

    if os.path.exists(path):
        shutil.rmtree(path)

    try:
        subprocess.run(
            ["git", "clone", repo_url, path],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ Repo cloned at: {path}")

    except subprocess.CalledProcessError as e:
        print("❌ Git clone failed")
        print(e.stderr)
        raise


def write_patch(repo_path, file_name, code):

    full_path = os.path.join(repo_path, file_name)

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w") as f:
        f.write(code)

    print(f"✅ Patch written to: {full_path}")


def commit_and_push(repo_path, branch_name):

    try:
        # 🔥 set git identity (IMPORTANT)
        subprocess.run(
            ["git", "config", "user.name", "AI Agent"],
            cwd=repo_path,
            check=True
        )
        subprocess.run(
            ["git", "config", "user.email", "ai-agent@example.com"],
            cwd=repo_path,
            check=True
        )

        # 🔥 create or switch branch safely
        subprocess.run(
            ["git", "checkout", "-B", branch_name],
            cwd=repo_path,
            check=True
        )

        # 🔥 add changes
        subprocess.run(
            ["git", "add", "."],
            cwd=repo_path,
            check=True
        )

        # 🔥 commit (skip if nothing to commit)
        commit = subprocess.run(
            ["git", "commit", "-m", "AI-generated fix"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )

        if "nothing to commit" in commit.stdout.lower():
            print("⚠️ Nothing to commit")
        else:
            print("✅ Commit created")

        # 🔥 push (IMPORTANT)
        subprocess.run(
            ["git", "push", "-u", "origin", branch_name, "--force"],
            cwd=repo_path,
            check=True
        )

        print(f"🚀 Changes pushed to branch: {branch_name}")

    except subprocess.CalledProcessError as e:
        print("❌ Git operation failed")
        print(e)
        raise