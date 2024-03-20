from src.two_pointers.trapping_rain_water import TrappingRainWaterSolution


def test_can_get_correct_answer():
    assert TrappingRainWaterSolution().solution(height = [4,2,0,3,2,5]) == 9