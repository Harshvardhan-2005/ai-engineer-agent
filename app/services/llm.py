def ask_llm(prompt: str) -> str:
    
    # 🧠 Planner behavior
    if "Break this issue into steps" in prompt:
        return """1. Locate login function
2. Check password validation
3. Add condition for empty password
4. Return proper error"""

    # 💻 Code generator behavior
    if "Fix the issue" in prompt:
        return """def login(username, password):
    if password == "":
        return "Error: Empty password"
    return "Success"
"""

    # 🧪 Test generator behavior
    if "Write tests" in prompt:
        return """def test_empty_password():
    assert login("user", "") == "Error: Empty password"
"""

    return "default response"