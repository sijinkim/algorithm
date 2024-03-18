from src.two_pointers.container_with_most_water import ContainerWithMostWaterSolution


def test_can_get_correct_answer():
    assert (
        ContainerWithMostWaterSolution().solution(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
        == 49
    )


def test_can_get_correct_answer_with_edge_case():
    assert ContainerWithMostWaterSolution().solution(height=[1, 4]) == 1


def test_can_get_zero_water():
    assert (
        ContainerWithMostWaterSolution().solution(
            height=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        )
        == 0
    )
