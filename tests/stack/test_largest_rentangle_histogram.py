from src.stack.largest_rectangle_histogram import LargestRectangleHistogram


def test_correct_answer():
    assert LargestRectangleHistogram().solution(heights=[2, 1, 5, 6, 2, 3]) == 10


def test_correct_answer_time():
    assert (
        LargestRectangleHistogram().solution_time_limit(heights=[2, 1, 5, 6, 2, 3])
        == 10
    )
