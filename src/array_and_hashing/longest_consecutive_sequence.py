"""
2024-01-26

128. Longest Consecutive Sequence (https://leetcode.com/problems/longest-consecutive-sequence)
"""
from pydantic import BaseModel

from src.utils import timer


class LongestConsecutiveSequenceSolution(BaseModel):
    nums: list[int]

    @timer
    def longest_consecutive(self) -> int:
        ...
