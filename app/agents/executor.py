from app.core.logger import log_event


def executor_agent(state):

    # Fail first 2 times, then pass
    if state["meta"]["iteration_count"] < 2:
        result = "fail"
    else:
        result = "pass"

    state["tests"]["status"] = result
    state["meta"]["iteration_count"] += 1

    log_event({
        "agent": "executor",
        "result": result,
        "iteration": state["meta"]["iteration_count"]
    })

    return state