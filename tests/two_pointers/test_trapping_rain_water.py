from src.two_pointers.trapping_rain_water import TrappingRainWaterSolution


def test_can_get_correct_answer():
    assert (
        TrappingRainWaterSolution().solution(
            height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        )
        == 6
    )


def test_can_get_correct_answer_with_edge_case():
    assert TrappingRainWaterSolution().solution(height=[4, 2, 3]) == 1


def test_can_get_correct_answer_using_recurssion():
    assert TrappingRainWaterSolution().recursive_solution(height=[4, 2, 3]) == 1
