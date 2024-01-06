"""
2023-01-06

242.Valid Anagram (https://leetcode.com/problems/valid-anagram)
"""
from collections import Counter

from pydantic import BaseModel, field_validator

from src import timer


class ValidAnagramSolution(BaseModel):
    s: str
    t: str

    @field_validator("s", "t")
    def check_length(cls, v: str) -> str:
        if len(v) < 1 or len(v) > 5 * 10**4:
            raise ValueError("1 <= s.length, t.length <= 5 * 10^4")
        return v

    @timer
    def is_anagram(self) -> bool:
        if not len(self.s) == len(self.t):
            return False

        s_counts = Counter(self.s)
        for i in self.t:
            if i not in s_counts:
                return False

            if s_counts[i] == 0:
                return False

            s_counts[i] -= 1

        return True

    @timer
    def is_anagram_faster(self) -> bool:
        if not len(self.s) == len(self.t):
            return False
        return Counter(self.s) == Counter(self.t)
