"""
2024-01-27

155.Min Stack (https://leetcode.com/problems/min-stack/)
"""


class MinStack:
    """
    self.min_value와 각 노드에 min 값 담기를 같이 할 이유가 있을까?
    """

    def __init__(self) -> None:
        self.stack: list[tuple[int, float]] = []

    def push(self, val: int) -> None:
        min_value = self.stack[-1][1] if len(self.stack) > 0 else float("inf")
        self.stack.append((val, min(val, min_value)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> float:
        return self.stack[-1][0]

    def get_min(self) -> float:
        return self.stack[-1][1]
