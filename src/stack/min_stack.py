"""
2024-01-27

155.Min Stack (https://leetcode.com/problems/min-stack/)
"""
from pydantic import BaseModel, Field


class MinStack(BaseModel):
    stack: list[dict[int, int]] = Field(default=[])
    # { 현재 노드 값: 현재 노드 포함, 지금까지 push된 값들 중 가장 작은 값}
    min_value: int = Field(default=0)

    def push(self, val: int) -> None:
        self.min_value = min(val, self.min_value)
        self.stack.append({val: self.min_value})

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return list(self.stack[-1].items())[0][0]

    def get_min(self) -> int:
        return list(self.stack[-1].items())[0][1]
