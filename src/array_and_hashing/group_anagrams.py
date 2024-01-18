"""
2024-01-18

49.Group Anagrams (https://leetcode.com/problems/group-anagrams)
"""
from pydantic import BaseModel

from src import timer


class GroupAnagramsSolution(BaseModel):
    strs: list[str]

    @timer
    def group_anagrams(self) -> list[list[str]]:
        check_pool: dict[tuple[frozenset[str], int], list[str]] = {}

        for s in self.strs:
            s_key = (frozenset(s), len(s))
            if s_key not in check_pool:
                check_pool[s_key] = [s]
            else:
                check_pool[s_key].append(s)

        return [sorted(v) for _, v in check_pool.items()]
