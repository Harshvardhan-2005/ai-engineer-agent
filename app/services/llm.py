def ask_llm(prompt: str) -> str:

    if "Break this issue" in prompt:
        return """1. Locate login function
2. Add empty password check
3. Return proper error"""

    if "Fix the issue" in prompt:
        return """def login(username, password):
    if password == "":
        return "Error: Empty password"
    return "Success"
"""

    if "Write tests" in prompt:
        return """from solution import login

def test_empty_password():
    assert login("user", "") == "Error: Empty password"
"""

    return "default response"