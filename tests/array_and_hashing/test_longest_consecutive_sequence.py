import pytest

from src.array_and_hashing import LongestConsecutiveSequenceSolution


@pytest.fixture
def nums():
    return [
        [100, 4, 200, 1, 3, 2],
        [11, 22, 33, 44, 55],
        [5, 3, 2, 1, 4, 1, 3, 2, 4, 5],
        [],
        [1, 2, 3, 3, 3, 3, 4, 5, 6, 7],
        [0],
    ]


def test_can_check_consecutive_sequence(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[0]).longest_consecutive_try() == 4
    )
    assert LongestConsecutiveSequenceSolution(nums=nums[0]).longest_consecutive() == 4
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[0]).longest_consecutive_develop()
        == 4
    )


def test_can_check_no_sequence(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[1]).longest_consecutive_try() == 1
    )
    assert LongestConsecutiveSequenceSolution(nums=nums[1]).longest_consecutive() == 1
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[1]).longest_consecutive_develop()
        == 1
    )


def test_can_check_duplicate_sequence(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[2]).longest_consecutive_try() == 5
    )
    assert LongestConsecutiveSequenceSolution(nums=nums[2]).longest_consecutive() == 5
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[2]).longest_consecutive_develop()
        == 5
    )


def test_can_check_empty_nums(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[3]).longest_consecutive_try() == 0
    )
    assert LongestConsecutiveSequenceSolution(nums=nums[3]).longest_consecutive() == 0
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[3]).longest_consecutive_develop()
        == 0
    )


def test_can_restart_counting(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[4]).longest_consecutive_try() == 7
    )
    assert LongestConsecutiveSequenceSolution(nums=nums[4]).longest_consecutive() == 7
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[4]).longest_consecutive_develop()
        == 7
    )


def test_can_check_single_element(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[5]).longest_consecutive_try() == 1
    )
    assert LongestConsecutiveSequenceSolution(nums=nums[5]).longest_consecutive() == 1
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[5]).longest_consecutive_develop()
        == 1
    )


def test_check_runtime_base(nums):
    assert LongestConsecutiveSequenceSolution(nums=nums[0]).longest_consecutive() == 4


def test_check_runtime_try(nums):
    assert (
        LongestConsecutiveSequenceSolution(nums=nums[0]).longest_consecutive_try() == 4
    )


def test_check_runtime_develop(nums):
    assert (
        LongestConsecutiveSequenceSolution(
            nums=[9, 1, -3, 2, 4, 8, 3, -1, 6, -2, -4, 7]
        ).longest_consecutive_develop()
        == 4
    )


def test_check_runtime_solution(nums):
    assert LongestConsecutiveSequenceSolution(nums=nums[0]).n_solution() == 4
