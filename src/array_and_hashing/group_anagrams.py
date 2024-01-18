"""
2024-01-18

49.Group Anagrams (https://leetcode.com/problems/group-anagrams)
"""
from pydantic import BaseModel

from src import timer


class GroupAnagramsSolution(BaseModel):
    strs: list[str]

    @timer
    def group_anagrams_fail(self) -> list[list[str]]:
        """
            runtime을 줄여야한다는 생각에 집중하여 dictionary의 구조의 장점을 활용하지 못함
            1) hash key를 사용해서 O(1)로 값을 비교해 runtime을 줄여야한다.
            2) strs item을 한번만 순회하고, 순회하면서 Counter key로 anagram 여부를 한번에 확인, anagram에 해당하는 item을 value에 리스트로 저장
            3) Counter가 unhashable type이라는 것을 확인 후, hashable하게 바꾸는 방법에 집중하면서 'anagram' 여부 확인 로직에서 멀어짐 (key로 표현할 수 있는 형태인지에 집중)
            4) hashable 하나, anagram 확인 테스트 케이스 커버 못함(test_can_check_same_length_strs())

            dictionary의 key:value 구조의 장점을 활용할 것

            key를 strs item으로, value를 해당 item의 Counter로 둔다면?
            value 확인하는 것만으로 anagram 여부 확인 가능
        """
        check_pool: dict[tuple[frozenset[str], int], list[str]] = {}

        for s in self.strs:
            s_key = (frozenset(s), len(s))
            if s_key not in check_pool:
                check_pool[s_key] = [s]
            else:
                check_pool[s_key].append(s)

        return [sorted(v) for _, v in check_pool.items()]
    
    @timer
    def group_anagrams(self) -> list[list[str]]:
        ...