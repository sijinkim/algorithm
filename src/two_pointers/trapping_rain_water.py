"""
2024-03-20
42. Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/)
"""
from collections import deque

from src.utils import timer


class TrappingRainWaterSolution:
    @timer
    def wrong_solution(self, height: list[int]) -> int:
        """
        제약사항
        n == height.length
        1 <= n <= 2 * 10_000 -> O(N*N)로 해결할 경우 runtime 1초 초과
        0 <= height[i] <= 100_000

        0. height에 대해 left wall, right wall(left wall <= right wall)을 서치
            left wall - right wall 기준 max water unit 계산 후,
            left wall 과 right wall 사이의 height 값 빼기
        1. left idx 설정: left = 0, right = left + 1
            1.1. if height[left] > height[right]: right += 1
            1.2. if height[left] <= height[right]: water volume 계산
            (right - left - 1) * height[left] - sum(height[left+1:right])
        2. if height[left] <= height[right] 상황이 없을 경우(height 끝까지 left wall과
            같거나 큰 value 없는 경우)
            left idx 재설정: left += 1 (1.부터 다시 시작)

        O(N*N) // 최악의 시나리오: left skewed. 모든 left wall에 대하여 끝까지 탐색하는 경우.

        실패한 이유: left wall보다 right wall 더 큰 경우 고려 안됨
        개선 방향: 모든 포지션에 대하여 left/right max 값을 찾고, 둘 중 min 값을 물이 채워질 수 있는 높이로
            -> point: 모든 포지션에 대하여 left/right 찾기를 O(n)으로 끝내야함
        """
        left = 0
        right = left + 1

        result = 0
        while left < len(height) - 1:
            if right == len(height):
                # height 끝까지 right wall 탐색한 경우
                # left wall wall 재설정
                left += 1
                right = left + 1
                continue

            if height[left] > height[right]:
                right += 1
                continue

            if height[left] <= height[right]:
                result += (right - left - 1) * height[left] - sum(
                    height[left + 1 : right]
                )
                # water units 계산 후 left wall 재설정
                left = right
                right = left + 1
                continue

        return result

    @timer
    def solution(self, height: list[int]) -> int:
        """
        0. height 1회 순회하면서, 각 idx 별 leftmax, rightmax 획득 => O(N) + O(N)
        1. height idx 별로, 각 idx에서 담을 수 있는 최대 water 계산 => O(N)
            1.1 기준 높이: min(leftmax, rightmax)
                if min(leftmax, rightmax) < height[idx]: 해당 idx에서는 물 담을 수 없음. pass
            1.2 min(leftmax, rightmax) >= height[idx]:
                담을 수 있는 물 idx 별 계산: min(leftmax, rightmax) - height[idx]
        2. idx 별 계산 값 총 합 return

        O(N)
        """
        # 계산상 편의를 위해 height 맨 앞과 뒤에 0 value 추가
        height_dq: deque[int] = deque(height)
        height_dq.appendleft(0)
        height_dq.append(0)

        result = 0
        leftmax = [0] * len(height_dq)
        rightmax = [0] * len(height_dq)

        # 각 idx 별 leftmax 세팅
        curr_left_max = 0  # init curr_left_max 0
        for i in range(1, len(height_dq)):
            # idx 별 leftmax 계산
            curr_left_max = max(curr_left_max, height_dq[i - 1])
            leftmax[i] = curr_left_max

        # 각 idx 별 rightmax 세팅
        curr_right_max = 0  # init curr_right_max 0
        for i in range(len(height_dq) - 2, -1, -1):
            # idx 별 rightmax 계산
            curr_right_max = max(curr_right_max, height_dq[i + 1])
            rightmax[i] = curr_right_max

        # 각 idx 별 max water units count
        for i in range(1, len(height_dq)):
            if min(leftmax[i], rightmax[i]) - height_dq[i] > 0:
                result += min(leftmax[i], rightmax[i]) - height_dq[i]
        return result
