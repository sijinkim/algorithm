"""
2024-01-26

20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
"""
from pydantic import BaseModel

from src.utils import timer


class ValidParenthesesSolution(BaseModel):
    s: str

    @timer
    def is_valid(self) -> bool:
        """
        0. s 순회하면서 괄호 타입별로, open/close 쌍 맞는지 체크

        O(N)
        0.0056ms
        """
        if not len(self.s) % 2 == 0:
            return False

        result: list[str] = []

        for item in self.s:
            if item in "([{":
                result.append(item)

            if item in "}])" and len(result) == 0:
                return False

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

    @timer
    def is_valid_with_stack(self) -> bool:
        """
        0. array를 stack으로 활용하여 O(N)
        1. opening bracket -> top
        2. closing bracket -> top check: type이 맞는가? opening이 맞는가?
            2.1 맞으면 pop
            2.2 틀리면 return False (elements 없는 경우도 False로 체크됨-length check)
        O(N)
        0.0045ms
        """
        stack: list[str] = []

        for item in self.s:
            if item in "([{":
                stack.append(item)

            if item in ")]}":
                try:
                    top_item = stack[-1]
                except:  # pylint: disable=bare-except
                    return False

                if item == ")" and top_item == "(":
                    pass
                elif item == "]" and top_item == "[":
                    pass
                elif item == "}" and top_item == "{":
                    pass
                else:
                    return False

                stack.pop()  # open된 쌍이 맞는 경우

        return len(stack) == 0
