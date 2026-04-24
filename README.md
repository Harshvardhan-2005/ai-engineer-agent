# AI Engineer Agent System

A stateful multi-agent system that autonomously processes GitHub issues by planning, generating code, writing tests, executing them, and iterating until success.

## Features

- Multi-agent architecture (Planner, Researcher, Coder, Tester, Reviewer, Executor)
- Stateful execution using LangGraph
- Retry loop with iteration control
- Structured logging for observability
- Mock LLM for deterministic testing

## Architecture

Input Issue → Planner → Researcher → Coder → Tester → Executor  
→ Retry Loop → Reviewer → Final Output

## Tech Stack

- Python
- LangGraph
- OpenAI (mocked)
- Logging + structured state

## Current Status

- Mock execution implemented
- Retry logic working
- Next: Docker-based execution & real repo parsing
