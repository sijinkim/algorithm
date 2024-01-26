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
        """
        0. O(N) time complexity로, 연속된 integer sequence max 길이 찾기
            -> base method: sorting 활용
        1. nums set sorting
        3. max_length=0, sorted nums 순회하면서
            3.1 다음 value와 현재 value가 1 차이 나는 경우 curr_length count up.
            3.2 다음 value와 현재 value가 1 차이 아닌 경우, curr_length 와 max_length 비교
            3.3 더 큰 값을 max_length로

        O(NlogN) + O(N)
        0.0264 ms
        """
        if len(self.nums) == 0:
            return 0

        sorted_nums_set: list[int] = sorted(list(set(self.nums)))  # O(NlogN) + O(N)

        max_length: int = 0
        curr_length: int = 1

        len_nums = len(sorted_nums_set)
        if len_nums == 1:
            return 1

        for i in range(len_nums - 1):  # O(N)
            if abs(sorted_nums_set[i] - sorted_nums_set[i + 1]) == 1:
                curr_length += 1

            else:
                curr_length = 1

            max_length = max(max_length, curr_length)

        return max_length
