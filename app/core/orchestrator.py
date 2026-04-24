from langgraph.graph import StateGraph

from app.agents.planner import planner_agent
from app.agents.researcher import researcher_agent
from app.agents.coder import coder_agent
from app.agents.tester import tester_agent
from app.agents.executor import executor_agent
from app.agents.reviewer import reviewer_agent


def build_graph():

    graph = StateGraph(dict)

    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("coder", coder_agent)
    graph.add_node("tester", tester_agent)
    graph.add_node("executor", executor_agent)
    graph.add_node("reviewer", reviewer_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "coder")
    graph.add_edge("coder", "tester")
    graph.add_edge("tester", "executor")

    def decision(state):

        if state["meta"]["iteration_count"] >= state["meta"]["max_iterations"]:
            state["status"] = "failed"
            return "__end__"

        if state["tests"]["status"] == "fail":
            return "coder"

    return "reviewer"

    graph.add_conditional_edges("executor", decision)

    graph.add_edge("reviewer", "__end__")

    return graph.compile()