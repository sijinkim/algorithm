"""
2024-03-05
704.Binary Search (https://leetcode.com/problems/binary-search/description/)
"""


class BinarySearchSolution:
    def solution(self, nums: list[int], target: int) -> int:
        """
        제한 사항
            1 <= nums.length <= 10_000
            -10_000 < nums[i], target < 10_000
            All the integers in nums are unique
            nums is sorted in ascending order

            O(log N) time complexity 안에 서치하기

            - 앞에서부터 순차 서치할 경우 O(N) 소요

        """
        min_idx: int = 0
        max_idx: int = len(nums) - 1
        pivot: int = max_idx // 2

        while min_idx <= max_idx:
            if nums[pivot] > target:
                max_idx = pivot - 1

            elif nums[pivot] < target:
                min_idx = pivot + 1

            elif nums[pivot] == target:
                return pivot

            pivot = (max_idx - min_idx) // 2 + min_idx
        return -1
