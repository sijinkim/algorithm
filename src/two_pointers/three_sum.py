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

        O(NlogN + N*N)
        """
        nums = sorted(nums)  # O(NlogN)
        result = []

        i = 0
        while i < len(nums) - 2:  # O(N)
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


