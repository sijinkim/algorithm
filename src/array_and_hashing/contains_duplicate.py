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

    @timer
    def duplicate_check_faster(self) -> bool:
        count: dict[int, int] = {}
        for n in self.nums:
            try:
                count[n] += 1
            except KeyError:
                count[n] = 1
            else:
                return True
        return False

    @timer
    def duplicate_check_more_faster(self) -> bool:
        return len(self.nums) > len(set(self.nums))

    def __repr__(self) -> str:
        return f"ContainsDuplicateSolution object: {id(self)}"
