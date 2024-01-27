"""
2024-01-27

155.Min Stack (https://leetcode.com/problems/min-stack/)
"""
from pydantic import BaseModel

class MinStack(BaseModel):
    val: int

    def __init__(self):
        ...

    def push(self) -> None:
        ...

    def pop(self) -> None:
        ...

    def top(self) -> int:
        ...

    def get_min(self) -> int:
        ...


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()