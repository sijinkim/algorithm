from src.two_pointers.three_sum import ThreeSumSolution


def test_can_get_correct_answer():
    assert ThreeSumSolution().solution(nums=[-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
    ]


def test_can_get_empty():
    assert ThreeSumSolution().solution(nums=[-1, 0, 3]) == []


def test_can_get_zeros():
    assert ThreeSumSolution().solution(nums=[0, 0, 0]) == [[0, 0, 0]]
