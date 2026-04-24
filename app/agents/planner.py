from app.services.llm import ask_llm
from app.core.logger import log_event


def planner_agent(state):
    prompt = f"""
    Break this issue into clear steps:

    Title: {state["issue"]["title"]}
    Description: {state["issue"]["description"]}
    """

    plan = ask_llm(prompt)

    steps = [step.split(".", 1)[-1].strip() for step in plan.split("\n") if step.strip()]

    state["plan"] = steps

    log_event({
        "agent": "planner",
        "steps": steps
    })

    return state