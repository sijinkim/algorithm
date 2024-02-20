from src.study import shift_and_rotate_solution


def test_can_get_correct_answer():
    rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ops = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

    assert shift_and_rotate_solution(rc=rc, operations=ops) == [
        [1, 6, 7, 8],
        [5, 9, 10, 4],
        [2, 3, 12, 11],
    ]
