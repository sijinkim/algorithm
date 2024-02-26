"""
2024-02-26

84. Largest Rectangle Histogram (https://leetcode.com/problems/largest-rectangle-in-histogram)
"""
from collections import deque

from src.utils import timer


class LargestRectangleHistogram:
    def solution_fail(self, heights: list[int]) -> int:
        """
        1 <= heights.length <= 100_000
        0 <= heights[i] <= 10_000

        1. 값이 있는 곳: 1, 값이 없는 곳: 0 으로 표기된 matrix 생성하여
            => 1-0 matrix 생성에 N * M (N: max(heights), M: heights.length)
        2. 행 별로 {max(연속된 1): ['연속된 1 위치 index', ... ] hash map 생성
            => 행 별 hash map 생성에 N * M
        3. dictionary 에서 가장 많이 나타난 1 index 조합 확인
            => 제일 뒤의 행 Pop 하더라도, max(연속된 1)이 다른 행에 존재하는지 count 하기 위해,
                max(연속된 1)보다 큰 key의 values 행마다 모두 검사 필요

        부적절한 알고리즘.
        """
        # 1-0 matrix 생성
        max_h: int = max(heights)
        new_matrix: deque[list[int]] = deque()

        for i in range(max_h):
            row: list[int] = []
            for idx, h in enumerate(heights):
                if h > 0:
                    row.append(1)
                    heights[idx] -= 1
                else:
                    row.append(0)
            new_matrix.appendleft(row)

        count_dict_list = []
        while new_matrix:
            check_row = new_matrix.pop()
            count_1 = 0
            index_1 = ""
            count_dict: dict[int, list[str]] = {}
            for i, v in enumerate(check_row):
                if v == 1:
                    index_1 = index_1 + f"{i}"
                    count_1 += 1
                    print(index_1, count_1)

                if v == 0 and count_1 != 0:
                    if count_1 not in count_dict:
                        count_dict[count_1] = []

                    count_dict[count_1].append(index_1)
                    count_1 = 0
                    index_1 = ""

                if i + 1 == len(check_row) and count_1 != 0:
                    count_dict[count_1] = []
                    count_dict[count_1].append(index_1)

            count_dict_list.append(count_dict)

        return 0

    @timer
    def solution_time_limit(self, heights: list[int]) -> int:
        """
        height.max 부터 pivot value 하나씩 카운트 다운 ( 0 < pivot <= height.max)
        1. pivot_value i 에 대하여
            1.1 heights 순회하면서
            1.2 pivot value 와 같거나 큰 값 카운트
            1.3 작은 경우
                1.3.2 카운트값 저장하고 카운트 0 초기화
        2. pivot value * max(카운트값): 해당 높이에서 가능한 최대 박스 사이즈
        3. 가장 큰 값 return


        O(N * M)
        N: max(heights)
        M: len(heights)
        """
        h: int = max(heights)

        area: list[int] = []
        while h >= 0:
            # height 별 가능한 박스 width 조사
            w_counts: list[int] = []
            w_tmp: list[int] = []
            for i, v in enumerate(heights):
                if v >= h:
                    w_tmp.append(i)
                    if i + 1 == len(heights):
                        w_counts.append(len(w_tmp))
                if v < h:
                    if w_tmp:
                        w_counts.append(len(w_tmp))
                    w_tmp = []

            area.append(h * max(w_counts))
            h -= 1

        return max(area)

    @timer
    def solution_time_limit2(self, heights: list[int]) -> int:
        """
        height.max 부터 pivot value 하나씩 카운트 다운 ( 0 < pivot <= height.max)
        1. pivot_value i 에 대하여
            1.1 heights 순회하면서
            1.2 pivot value 와 같거나 큰 값 카운트
            1.3 작은 경우
                1.3.2 카운트값 저장하고 카운트 0 초기화
        2. pivot value * max(카운트값): 해당 높이에서 가능한 최대 박스 사이즈
        3. 현재까지 가장 큰 값 기준으로, 더 살펴봐야하는 height thresh 설정 -> search pool 줄이기
        3. 가장 큰 값 return


        O(N * M)
        N: max(heights)
        M: len(heights)
        """
        h: int = max(heights)
        result: int = 0

        thresh: int | float = 0
        while h >= thresh:
            # height 별 가능한 박스 width 조사
            w_counts: list[int] = []
            w_tmp: list[int] = []
            for i, v in enumerate(heights):
                if v >= h:
                    w_tmp.append(i)
                    if i + 1 == len(heights):
                        w_counts.append(len(w_tmp))
                if v < h:
                    if w_tmp:
                        w_counts.append(len(w_tmp))
                    w_tmp = []

            area_tmp = h * max(w_counts)
            result = max(result, area_tmp)

            h -= 1
            thresh = result / len(heights)

        return result

    @timer
    def solution(self, heights: list[int]) -> int:
        """
        O(N) 풀이법

        heights[i] 별로, left smaller/right smaller 가 결국 heichts[i]를 h로 하는 블록의 최대 width
        1. heights 순회하면서 => O(N)
        2. 현재 heights가 최근 heights 보다 작니?
            2.1 작으면, area 계산
                2.1.1 현재 heights보다 큰 heights들에 대해 area 계산
                2.1.2 현재 heights와 같거나 작으면, width 이어질 수 있으므로 stop
        3. width stack에 push
        """
        result: int = 0
        width_stack: list[int] = [-1]

        heights.append(0)  # width_stack[-1], 무조건 0으로 세팅
        max_width: int = len(heights)
        for i in range(max_width):
            while (
                heights[i] < heights[width_stack[-1]]
            ):  # block이 끊기는 순간(smallest height를 만남)
                height = heights[width_stack.pop()]
                width = i - width_stack[-1] - 1  # width_stack[-1]: 계산하려는 block 앞 index
                result = max(result, height * width)
            width_stack.append(i)

        return result
