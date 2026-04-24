from app.services.llm import ask_llm
from app.core.logger import log_event


def coder_agent(state):
    prompt = f"""
    Fix the issue:
    {state["issue"]["description"]}

    Files:
    {state["context"]["relevant_files"]}
    """

    patch = ask_llm(prompt)

    state["solution"]["patch"] = patch   # ✅ FIXED

    log_event({
        "agent": "coder",
        "patch_length": len(patch)
    })

    return state