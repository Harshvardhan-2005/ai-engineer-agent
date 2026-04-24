from pydantic import BaseModel
from typing import List, Dict, Any


class Issue(BaseModel):
    title: str
    description: str
    repo: str
    issue_id: int


class Context(BaseModel):
    relevant_files: List[str] = []
    code_snippets: List[str] = []


class Solution(BaseModel):
    patch: str = ""
    explanation: str = ""


class Tests(BaseModel):
    generated_tests: str = ""
    execution_logs: str = ""
    status: str = ""  # pass / fail


class Review(BaseModel):
    feedback: str = ""
    approved: bool = False


class Meta(BaseModel):
    iteration_count: int = 0
    max_iterations: int = 5
    history: List[Dict[str, Any]] = []


class AgentState(BaseModel):
    issue: Issue
    plan: List[str] = []
    context: Context = Context()
    solution: Solution = Solution()
    tests: Tests = Tests()
    review: Review = Review()
    meta: Meta = Meta()
    status: str = "in_progress"