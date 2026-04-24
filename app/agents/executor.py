from app.tools.docker_exec import run_code_in_docker
from app.core.logger import log_event


def executor_agent(state):

    result = run_code_in_docker(
        state["solution"]["patch"],
        state["tests"]["generated_tests"]
    )

    status = "pass" if result["success"] else "fail"

    state["tests"]["status"] = status

    # ✅ structured logs
    state["tests"]["execution_logs"] = {
    "success": result.get("success", False),
    "stdout": result.get("stdout", ""),
    "stderr": result.get("stderr", ""),
    "execution_time": result.get("execution_time", 0)   # 👈 ADD THIS

    }

    state["meta"]["iteration_count"] += 1

    log_event({
        "agent": "executor",
        "status": status,
        "iteration": state["meta"]["iteration_count"]
    })

    return state