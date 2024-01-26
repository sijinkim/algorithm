"""
2024-01-26

20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
"""
from pydantic import BaseModel


class ValidParenthesesSolution(BaseModel):
    s: str

    def is_valid(self) -> bool:
        """
        0. s 순회하면서 괄호 타입별로, open/close 쌍 맞는지 체크

        O(N)
        """
        if not len(self.s) % 2 == 0:
            return False

        result: list[str] = []

        for item in self.s:
            if item in "([{":
                result.append(item)

            if item in "}])" and len(result) > 0:
                if item == "}" and result[-1] == "{":
                    result.pop()
                elif item == "]" and result[-1] == "[":
                    result.pop()
                elif item == ")" and result[-1] == "(":
                    result.pop()
                else:
                    return False

        return len(result) == 0
