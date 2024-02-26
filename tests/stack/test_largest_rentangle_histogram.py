from src.stack.largest_rectangle_histogram import LargestRectangleHistogram


def test_correct_answer():
    assert LargestRectangleHistogram().solution(heights=[2, 1, 5, 6, 2, 3]) == 10
