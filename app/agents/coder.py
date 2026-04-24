from app.services.llm import ask_llm
from app.core.logger import log_event
from app.tools.file_utils import write_patch


def coder_agent(state):

    prompt = f"""
    Fix the issue:
    {state["issue"]["description"]}
    """

    patch = ask_llm(prompt)

    state["solution"]["patch"] = patch

    repo_path = state["context"]["repo_path"]

    file_name = "solution.py"

    print("DEBUG repo_path:", repo_path)   # 👈 ADD THIS
    print("DEBUG writing file:", file_name)

    write_patch(repo_path, file_name, patch)

    log_event({
        "agent": "coder",
        "file_written": file_name
    })

    print(f"📝 Patch applied to {file_name}")

    return state