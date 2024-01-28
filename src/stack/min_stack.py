"""
2024-01-27

155.Min Stack (https://leetcode.com/problems/min-stack/)
"""
from typing import cast


class MinStack:
    """
    self.min_value와 각 노드에 min 값 담기를 같이 할 이유가 있을까?
    """
    def __init__(self) -> None:
        self.stack: list[dict[int | None, int | None]] = [{None: None}]
        self.min_value: int | None = None

    def push(self, val: int) -> None:
        if not self.min_value is None:
            self.min_value = min(val, self.min_value)
        else:
            self.min_value = val

        self.stack.append({val: self.min_value})

    def pop(self) -> None:
        self.stack.pop()
        self.min_value = list(self.stack[-1].items())[0][1]

    def top(self) -> int:
        return cast(int, list(self.stack[-1].items())[0][0])

    def get_min(self) -> int:
        return self.min_value
