"""
2024-01-18

49.Group Anagrams (https://leetcode.com/problems/group-anagrams)
"""
from pydantic import BaseModel


class GroupAnagramsSolution(BaseModel):
    strs: list[str]

    def group_anagrams(self) -> list[list[str]]:
        check_pool: dict[tuple[set[str], int], list[str]] = {}

        for s in self.strs:
            s_key = (set(s), len(s))
            if s_key not in check_pool:
                check_pool[s_key] = [s]
            else:
                check_pool[s_key].append(s)

        return [v for _,v in check_pool]
