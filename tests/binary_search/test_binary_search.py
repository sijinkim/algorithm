from src.binary_search.binary_search import BinarySearchSolution


def test_get_correct_answer():
    assert BinarySearchSolution().solution(nums=[-1, 0, 3, 5, 9, 12], target=9) == 4


def test_get_correct_answer_with_single_element():
    assert BinarySearchSolution().solution(nums=[100], target=100) == 0


def test_target_does_not_exist():
    assert BinarySearchSolution().solution(nums=[-1, 0, 3, 5, 9, 12], target=15) == -1
