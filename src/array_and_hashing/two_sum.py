"""
2023-1-10

1. Two Sum (https://leetcode.com/problems/two-sum/)
"""
from pydantic import BaseModel


class TwoSumSolution(BaseModel):
    nums: list[int]
    target: int

    def two_sum(self) -> list[int]:
        """
        1. nums item 하나씩 돌면서 다른 item과 더해 target과 동일한지 확인
            O(n^2)
        """
        ...
