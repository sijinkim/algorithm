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

    @timer
    def longest_consecutive_try(self) -> int:
        """
        0. O(N*N) 으로 푸는 방법. -> i가 단순히 카운트 업하는 연산이어도 O(N*N) 소요.
        1. nums hash 생성: hash key로 nums values 담음
        2. nums keys 순회하면서
            2.1 현재 key + i 값이 keys에 있는지 확인 (i < len(keys)) # 현재 key보다 큰 consecutive sequence
            2.2 현재 key - i 값이 keys에 있는지 확인 (i < len(keys)) # 현재 key보다 작은 consecutive sequence

        O(N^2)
        0.0371ms
        """
        if len(self.nums) == 0:
            return 0

        nums_dict: dict[int, int] = {}
        for n in self.nums:
            nums_dict[n] = 1  # consecutive sequence self count

        nums_keys = list(nums_dict.keys())
        curr_length: int = 0
        for n in nums_keys:  # bigger sequence
            for i in range(1, len(nums_keys)):
                if n + i in nums_dict:
                    curr_length += 1
                else:
                    break
            nums_dict[n] += curr_length
            curr_length = 0

        for n in nums_keys:  # smaller sequence
            for i in range(1, len(nums_keys)):
                if n - i in nums_dict:
                    curr_length += 1
                else:
                    break
            nums_dict[n] += curr_length
            curr_length = 0

        return max(nums_dict.values())
