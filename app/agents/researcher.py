from app.core.logger import log_event


def researcher_agent(state):
    # TEMP: simulate file discovery
    state["context"]["relevant_files"] = ["app/auth.py", "app/login.py"]

    log_event({
        "agent": "researcher",
        "files": state["context"]["relevant_files"]
    })

    return state