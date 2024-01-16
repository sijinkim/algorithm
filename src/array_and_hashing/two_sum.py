"""
2023-1-10

1. Two Sum (https://leetcode.com/problems/two-sum/)
"""
from pydantic import BaseModel, computed_field

from src import timer


class Num(BaseModel):
    value: int
    idx: int


def merge_sort(arr: list[Num]) -> list[Num]:
    left_arr: list[Num] = []
    right_arr: list[Num] = []

    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]

        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        # merge
        i = 0  # left_arr idx
        j = 0  # right_arr idx
        k = 0  # merged array idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i].value <= right_arr[j].value:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # 한쪽의 ordering 다 끝난 경우
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1

    return arr


class TwoSumSolution(BaseModel):
    nums: list[int]
    target: int

    @computed_field  # type: ignore[misc]
    @property
    def nums_with_idx(self) -> list[Num]:
        num_idx_list = []
        for idx, n in enumerate(self.nums):
            num_idx_list.append(Num(value=n, idx=idx))
        return num_idx_list

    @timer
    def two_sum(self) -> list[int]:
        """
        1. nums item 하나씩 돌면서 다른 item과 더해 target과 동일한지 확인 =>  O(n^2)
        """
        result: list[int] = []
        for n in self.nums_with_idx:
            count = 1
            while n.idx + count < len(self.nums_with_idx):
                if n.value + self.nums_with_idx[n.idx + count].value == self.target:
                    result = [n.idx, n.idx + count]
                    break
                count += 1
            if len(result) == 2:
                break
        return result

    @timer
    def two_sum_with_sort(self) -> list[int]:
        """
        1. nums item 정렬(Merge Sort) => O(nlogn)
        2. 정렬된 nums Tree 사용, Binary search => O(nlogn)

        + 정렬 전 idx 기억 필요.. => Num dataclass 적용(value, idx 기억 용도)
        """
        #

        # merge sort
        sorted_list = merge_sort(self.nums_with_idx)

        # binary search
        result: list[int] = []
        for idx, n in enumerate(sorted_list):
            search_target = self.target - n.value
            search_pool = sorted_list[idx + 1 :]
            search_idx = idx + 1

            while len(result) == 0:
                pivot_idx = len(search_pool) // 2

                # 더이상 left가 없을 때
                if pivot_idx == 0:
                    if search_pool[pivot_idx].value == search_target:
                        result = [idx, search_idx + pivot_idx]
                    else:
                        break

                # 더이상 right가 없을 때
                if pivot_idx == len(search_pool) - 1:
                    if search_pool[pivot_idx].value == search_target:
                        result = [idx, search_idx + pivot_idx]
                    elif search_pool[pivot_idx - 1].value == search_target:
                        result = [idx, search_idx + pivot_idx - 1]
                    else:
                        break

                if search_pool[pivot_idx].value == search_target:
                    result = [idx, search_idx + pivot_idx]
                elif search_pool[pivot_idx].value > search_target:
                    search_pool = search_pool[:pivot_idx]
                else:
                    search_pool = search_pool[pivot_idx + 1 :]
                    search_idx = search_idx + pivot_idx + 1

            if result:
                break

        return [sorted_list[result[0]].idx, sorted_list[result[1]].idx]

    @timer
    def two_sum_faster_and_simpler(self) -> list[int]:
        num_idx_dict: dict[int, int] = {}
        result: list[int] = []
        for idx, n in enumerate(self.nums):
            if self.target - n in num_idx_dict:
                result = [num_idx_dict[self.target - n], idx]
                break
            num_idx_dict[n] = idx

        return result
