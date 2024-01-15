import random
import sys

from src.array_and_hashing import Num, TwoSumSolution, merge_sort

sys.setrecursionlimit(10**7)


def test_can_get_correct_answer():
    nums = [2, 7, 11, 15]
    target = 9

    assert TwoSumSolution(nums=nums, target=target).two_sum() == [0, 1]


def test_can_get_correct_answer_with_different_order():
    nums = [2, 11, 7, 15]
    target = 9

    assert TwoSumSolution(nums=nums, target=target).two_sum() == [0, 2]


def test_can_get_correct_answer_with_negative_target():
    nums = [-11, 3, -100, 5, 8]
    target = -95

    assert TwoSumSolution(nums=nums, target=target).two_sum() == [2, 3]


def test_can_get_correct_answer_with_duplicate_nums():
    nums = [3, 3]
    target = 6

    assert TwoSumSolution(nums=nums, target=target).two_sum() == [0, 1]


def test_can_get_correct_answer_faster():
    nums = [2, 7, 11, 15]
    target = 9

    assert TwoSumSolution(nums=nums, target=target).two_sum_with_sort() == [0, 1]


def test_can_get_correct_answer_with_different_order_faster():
    nums = [2, 11, 7, 15]
    target = 9

    assert TwoSumSolution(nums=nums, target=target).two_sum_with_sort() == [0, 2]


def test_can_get_correct_answer_with_negative_target_faster():
    nums = [-11, 3, -100, 5, 8]
    target = -95

    assert TwoSumSolution(nums=nums, target=target).two_sum_with_sort() == [2, 3]


def test_can_get_correct_answer_with_duplicate_nums_faster():
    nums = [3, 3]
    target = 6

    assert TwoSumSolution(nums=nums, target=target).two_sum_with_sort() == [0, 1]


def test_merge_sort():
    nums = [5, 3, 10, 6, 7, 8, 2, 1, 9, 4]
    for idx, n in enumerate(nums):
        nums[idx] = Num(value=n, idx=idx)

    result: list[int] = []
    for n in merge_sort(nums):
        result.append(n.value)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_can_get_correct_answer_faster_2():
    nums = [3, 2, 3]
    target = 6

    assert TwoSumSolution(nums=nums, target=target).two_sum_with_sort() == [0, 2]

def test_can_get_correct_answer_faster_3():
    nums = [2, 5, 5, 11]
    target = 10

    assert TwoSumSolution(nums=nums, target=target).two_sum_with_sort() == [1, 2]
