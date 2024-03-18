"""
2024-03-18

11. Container With Most Water (https://leetcode.com/problems/container-with-most-water)
"""
from src.utils import timer


class ContainerWithMostWaterSolution:
    @timer
    def solution(self, height: list[int]) -> int:
        """
        1. min_idx: 0, max_idx: len(height)-1 => get height[min_idx], height[max_idx]
        2. calc the area of water by min_idx, max_idx and then update the max area or not.
        3. compare height[min_idx] with height[max_idx] while min_idx < max_idx
            3.1 if height[min_idx] =< height[max_idx]: min_idx + 1
            3.2 if height[min_idx] > height[max_idx]: max_idx - 1
        4. return the max area value of water

        O(N)
        """
        min_idx = 0
        max_idx = len(height) - 1

        max_water = 0
        while min_idx < max_idx:
            left = height[min_idx]
            right = height[max_idx]

            curr_water = (max_idx - min_idx) * min(left, right)
            max_water = max(max_water, curr_water, 0)

            if left > right:
                max_idx -= 1
            else:
                min_idx += 1

        return max_water
