# AI Engineer Agent (Multi-Agent System)

A stateful multi-agent system that autonomously processes software issues by:
- Planning tasks
- Analyzing code context
- Generating fixes
- Writing tests
- Iterating until validation success

## 🚀 Key Features

- Multi-agent architecture (Planner, Researcher, Coder, Tester, Executor, Reviewer)
- Stateful execution with shared memory
- Retry loop with convergence control
- Structured logging for observability
- Deterministic mock LLM for testing

## 🧠 Architecture

Issue → Planner → Research → Code → Test → Execute  
→ Retry Loop → Reviewer → Final Output

## ⚙️ Tech Stack

- Python
- LangGraph (stateful orchestration)
- Mock LLM (OpenAI-compatible)
- Structured logging

## 📊 Results

- Iterative execution with failure recovery
- Converges in ~3 iterations (mock setup)
- Fully traceable execution flow

## 🔜 Next Steps

- Docker-based code execution
- GitHub API integration
- Real repository parsing
- Evaluation metrics
