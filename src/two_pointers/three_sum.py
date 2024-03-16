"""
2024-03-14
15. 3Sum (https://leetcode.com/problems/3sum/)
"""
from src.utils import timer
from collections import defaultdict


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

    @timer
    def solution_faster(self, nums: list[int]) -> list[list[int]]:
        """
        1. i는 고정
        2. j - min, k - max 사용하여 [j] + [k] = 0 - [i] 인지 확인
            2.1 i 마다 위 과정 반복, 
            2.2 그런데 j,k 옮겨가면서 반복 확인하는 게 아니라 한번 확인한 pair의 값은 기억해놓는다면?
                => dictionary key: [j] + [k], value: [(j, k)]

        O(NlogN + N*N) 동일하나, 탐색 N*N 하는 횟수 줄임
        """
        nums = sorted(nums)  # O(NlogN)
        pairs = defaultdict(list)
        result = []

        i = 0
        while i < len(nums) - 2:  # O(N)
            j = i + 1
            k = len(nums) - 1
            target = 0 - nums[i]
            from_dict = False

            if target in pairs:
                for p in pairs[target]:
                    if p[0] > i:
                        result.append((nums[i], nums[p[0]], nums[p[1]]))
                        from_dict = True
                
                if from_dict:
                    i += 1
                    from_dict = False
                    continue

            while j < k:  # O(N)
                pair_sum = nums[j] + nums[k]
                
                if pair_sum not in pairs:
                    pairs[pair_sum].append([j, k])

                if pair_sum < target:
                    j += 1

                elif pair_sum > target:
                    k -= 1

                else:  # nums[i] + nums[k] == target
                    result.append((nums[i], nums[j], nums[k]))
                    j += 1
            i += 1

        return sorted(list(map(lambda x: list(x), set(result))))
