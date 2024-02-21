from src.study import develop_function_solution


def test_get_correct_answer():
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    assert develop_function_solution(progresses=progresses, speeds=speeds) == [2, 1]


def test_get_correct_answer_with_edge_case():
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    assert develop_function_solution(progresses=progresses, speeds=speeds) == [1, 3, 2]
