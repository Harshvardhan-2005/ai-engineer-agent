from app.core.state import AgentState, Issue
from app.core.orchestrator import build_graph


def run():

    issue = Issue(
        title="Fix login bug",
        description="Login fails when password is empty",
        repo="test/repo",
        issue_id=1
    )

    state = AgentState(issue=issue)

    graph = build_graph()

    result = graph.invoke(state.model_dump())

    print(result)


if __name__ == "__main__":
    run()