from app.services.llm import ask_llm
from app.core.logger import log_event


def tester_agent(state):
    prompt = f"""
    Write tests for this code:
    {state["solution"]["patch"]}
    """

    tests = ask_llm(prompt)

    state["tests"]["generated_tests"] = tests

    log_event({
        "agent": "tester"
    })

    return state