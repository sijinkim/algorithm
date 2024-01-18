"""
2024-01-18

49.Group Anagrams (https://leetcode.com/problems/group-anagrams)
"""
from pydantic import BaseModel
from collections import Counter

class GroupAnagramsSolution(BaseModel):
    strs: list[str]

    def group_anagrams(self) -> list[list[str]]:
        check_pool: dict[Counter, list[str]] = {}

        for s in self.strs:
            s_set = Counter(s)
            if s_set not in check_pool:
                check_pool[s_set] = [s]
            else:
                check_pool[s_set].append(s)
        
        return [v for _,v in check_pool]