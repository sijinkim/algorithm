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
        """
            BFS
            
            0.1195ms
        """
        check_list: list[str] = ["("]
        while len(check_list) > 0 and len(check_list[0]) < 2 * self.n:
            top = check_list.pop(0)
            counter = Counter(top)
            if counter["("] < self.n:
                check_list.append(top + "(")

            if counter["("] > counter[")"]:
                check_list.append(top + ")")
        return check_list

    @timer
    def generate_parenthesis_dfs(self) -> list[str]:
        """
            DFS

            0.0360ms
        """
        result: list[str] = []

        def dfs(open_par: int, close_par: int, combination: str) -> None:
            if open_par == self.n and close_par == self.n:
                result.append(combination)

            if open_par < self.n:
                dfs(open_par + 1, close_par, combination + "(")

            if open_par > close_par:
                dfs(open_par, close_par + 1, combination + ")")

        dfs(open_par=0, close_par=0, combination="")
        return result
