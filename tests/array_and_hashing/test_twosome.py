from src.array_and_hashing import TwoSumSolution


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
