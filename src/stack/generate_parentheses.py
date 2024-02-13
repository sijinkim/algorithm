"""
2024-02-13

22.Generate Parentheses (https://leetcode.com/problems/generate-parentheses)
"""
from collections import Counter

from pydantic import BaseModel, field_validator

from src.utils import timer


class GenerateParenthesesSolution(BaseModel):
    n: int

    @field_validator("n")
    def check_value(cls, v: int) -> int:
        if v < 1 or v > 8:
            raise ValueError("1 <= n <= 8")
        return v

    @timer
    def generate_parenthesis(self) -> list[str]:
        check_list: list[str] = ["("]
        while len(check_list) > 0 and len(check_list[0]) < 2 * self.n:
            top = check_list.pop(0)
            counter = Counter(top)
            if counter["("] < self.n:
                check_list.append(top + "(")

            if counter["("] > counter[")"]:
                check_list.append(top + ")")
        return check_list
