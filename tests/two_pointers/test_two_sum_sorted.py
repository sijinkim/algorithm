from src.two_pointers.two_sum_sorted import TwoSumSolution


def test_can_get_correct_answer():
    assert TwoSumSolution().solution(numbers=[2, 7, 11, 15], target=9) == [1, 2]


def test_can_get_target_zero():
    assert TwoSumSolution().solution(numbers=[-1, 0, 0, 3, 5], target=0) == [2, 3]


def test_can_get_correct_answer_faster():
    assert TwoSumSolution().solution_faster(numbers=[2, 7, 11, 15], target=9) == [1, 2]


def test_can_get_target_zero_faster():
    assert TwoSumSolution().solution_faster(numbers=[-1, 0, 0, 3, 5], target=0) == [
        2,
        3,
    ]
