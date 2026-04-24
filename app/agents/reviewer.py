from app.core.logger import log_event


def reviewer_agent(state):
    approved = state["tests"]["status"] == "pass"

    state["review"]["approved"] = approved

    if approved:
        state["status"] = "success"
    else:
        state["status"] = "failed"

    return state