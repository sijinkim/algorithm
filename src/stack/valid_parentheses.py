"""
2024-01-26

20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
"""
from pydantic import BaseModel

class ValidParenthesesSolution(BaseModel):
    s: str

    def is_valid(self) -> bool:
        ...