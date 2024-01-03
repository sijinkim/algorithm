"""
2024-01-03

217.Contains Duplicate(https://leetcode.com/problems/contains-duplicate)
"""
from collections import Counter

from pydantic import BaseModel

from src import timer


class ContainsDuplicateSolution(BaseModel):
    nums: list[int]

    @timer
    def duplicate_check(self) -> bool:
        num_counter = Counter(self.nums)
        if num_counter.total() > len(num_counter):
            return True
        return False

    def __repr__(self) -> str:
        return f"ContainsDuplicateSolution object: {id(self)}"
