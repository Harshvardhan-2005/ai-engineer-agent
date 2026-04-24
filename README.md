# 🤖 AI Engineer Agent (Multi-Agent System)

A stateful multi-agent system that autonomously processes software issues by:
- Planning tasks
- Analyzing code context
- Generating fixes
- Writing tests
- Iterating until validation success

This system mimics a real software engineering workflow using autonomous agents with iterative self-correction.

---

## 🚀 Key Features

- Multi-agent architecture (Planner, Researcher, Coder, Tester, Executor, Reviewer)
- Stateful execution with shared memory
- Retry loop with convergence control
- Structured logging for observability
- Deterministic mock LLM for testing

---

## 🧠 Architecture

<p align="center">
  <img src="./docs/multi.svg" width="800"/>
</p>

<p align="center">
  <i>Multi-agent execution pipeline with retry loop and decision-based flow</i>
</p>

---

## 📊 Execution Flow

```text
Issue
  ↓
Planner
  ↓
Researcher
  ↓
Coder
  ↓
Tester
  ↓
Executor
  ↓
Decision
   ├── Retry (loop back)
   └── Reviewer → Final Output
```

---

## Project Structure 
```text
ai-engineer-agent/
│
├── app/
│   ├── agents/              # Individual agents (core logic units)
│   │   ├── planner.py
│   │   ├── researcher.py
│   │   ├── coder.py
│   │   ├── tester.py
│   │   ├── executor.py
│   │   └── reviewer.py
│   │
│   ├── core/                # Orchestration + system backbone
│   │   ├── orchestrator.py
│   │   ├── state.py
│   │   ├── logger.py
│   │   └── config.py
│   │
│   ├── services/            # External integrations (LLM, metrics)
│   │   ├── llm.py
│   │   └── metrics.py
│   │
│   ├── tools/               # Utilities (future integrations)
│   │   ├── github.py
│   │   ├── docker_exec.py
│   │   └── file_utils.py
│   │
│   └── main.py              # Entry point
│
├── docs/                    # Architecture diagrams
│   └── multi.svg
│
├── logs/                    # Execution logs
│   └── system.log
│
├── tests/                   # (optional) test cases
│
├── .env                     # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```
## ⚙️ Tech Stack

- Python  
- LangGraph (stateful orchestration)  
- Mock LLM (OpenAI-compatible)  
- Structured logging  

---

## 📊 Results

- Iterative execution with failure recovery  
- Converges in ~3 iterations (mock setup)  
- Fully traceable execution flow  

---

## 🔜 Next Steps

- Docker-based code execution  
- GitHub API integration  
- Real repository parsing  
- Evaluation metrics  
