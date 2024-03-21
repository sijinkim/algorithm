"""
2024-03-14
15. 3Sum (https://leetcode.com/problems/3sum/)
"""
from src.utils import timer


class ThreeSumSolution:
    # pylint: disable=unnecessary-lambda
    @timer
    def solution(self, nums: list[int]) -> list[list[int]]:
        """
        i != j != k 일 때, nums[i] + nums[j] + nums[k] == 0 인 조합 찾기

        제약 사항
        3 <= nums.length <= 3000
        -100_000 <= nums[i] <= 100_000

        O(NlogN + N*N):
        결국 최소로 two sum 조합찾는 방법 O(N).
        O(N)을 target N에 대하여 계산 필요.

        target N에 대하여 반복 수행되는 조합 서치과정을 줄이기
        -> 이미 조합 찾아본 target 값이면 pass
        """
        nums = sorted(nums)  # O(NlogN)
        result = []

        i = 0
        while i < len(nums) - 2:  # O(N)
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]
            while j < k:  # O(N)
                if nums[j] + nums[k] < target:
                    j += 1

                elif nums[j] + nums[k] > target:
                    k -= 1

                else:  # nums[i] + nums[k] == target
                    result.append((nums[i], nums[j], nums[k]))
                    j += 1
            i += 1

        return sorted(list(map(lambda x: list(x), set(result))))
