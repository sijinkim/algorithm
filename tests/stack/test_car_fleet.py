from src.stack import CarFleetSolution


def test_can_get_correct_answer():
    assert (
        CarFleetSolution(
            target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]
        ).solution()
        == 3
    )


def test_can_get_correct_answer_with_single_car():
    assert CarFleetSolution(target=10, position=[3], speed=[3]).solution() == 1
