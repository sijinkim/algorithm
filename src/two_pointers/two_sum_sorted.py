"""
2024-03-11
167. Two Sum II - Input Array Is Sorted 
(https://leetcode.com/problems/two-sum-ii-input-array-is-sorted)
"""


class TwoSumSolution:
    def solution(self, numbers: list[int], target: int) -> list[int]:
        """
        조건
        0. numbers: sorted list (non-decreasing order)
        1. 1 <= index1 < index2 <= numbers.length
        2. 2 <= numbers.length <= 3 * 10_000
        3. exactly one solution

        O(N*N)
        """
        answer: list[int] = []
        idx = 0
        while not answer:
            num1 = numbers[idx]
            num2 = target - num1

            for num2_idx in range(idx + 1, len(numbers)):
                if num2 == numbers[num2_idx]:
                    answer = [idx + 1, num2_idx + 1]
            idx += 1

        return answer

    def solution_faster(self, numbers: list[int], target: int) -> list[int]:
        """
        O(N)
        """
        min_idx = 0
        max_idx = len(numbers) - 1

        answer: list[int] = []
        while min_idx < max_idx:
            min_max_sum = numbers[min_idx] + numbers[max_idx]
            if min_max_sum > target:
                max_idx -= 1

            elif min_max_sum < target:
                min_idx += 1

            else:
                answer = [min_idx + 1, max_idx + 1]
                break

        return answer
