from src.two_pointers.two_sum_sorted import TwoSumSolution

def test_can_get_correct_answer():
    assert TwoSumSolution().solution(numbers = [2,7,11,15], target = 9) == [1,2]