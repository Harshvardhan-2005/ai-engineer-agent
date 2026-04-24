import subprocess
import uuid
import os
import shutil
import time
import re


def run_code_in_docker(code: str, tests: str):

    run_id = str(uuid.uuid4())
    base_path = f"/tmp/agent_run_{run_id}"

    os.makedirs(base_path, exist_ok=True)

    try:
        with open(f"{base_path}/solution.py", "w") as f:
            f.write(code)

        with open(f"{base_path}/test_solution.py", "w") as f:
            f.write(tests)

        cmd = [
            "docker", "run", "--rm",
            "-v", f"{base_path}:/app",
            "-w", "/app",
            "python:3.11",
            "sh", "-c",
            "pip install pytest >/dev/null 2>&1 && pytest -q"
        ]

        start_time = time.time()

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=10
        )

        end_time = time.time()

        execution_time = round(end_time - start_time, 3)
        success = result.returncode == 0

        matches = re.findall(r"(\d+\.\d+)\s*s", result.stdout)
        test_time = float(matches[-1]) if matches else None

        return {
            "success": success,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "execution_time": execution_time,
            "test_time": test_time
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": "Execution timed out",
            "execution_time": 10,
            "test_time": None
        }

    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "execution_time": 0,
            "test_time": None
        }

    finally:
        shutil.rmtree(base_path, ignore_errors=True)