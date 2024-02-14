from src.stack import NextGreaterElementSolution


def test_correct_answer():
    assert NextGreaterElementSolution().solution(
        nums1=[4, 1, 2], nums2=[1, 3, 4, 2]
    ) == [-1, 3, -1]
