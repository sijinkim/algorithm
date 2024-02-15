from src.stack import DailyTemperaturesSolution


def test_correct_answer():
    assert DailyTemperaturesSolution().daily_temperatures(
        temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_correct_answer_case1():
    assert DailyTemperaturesSolution().daily_temperatures(
        temperatures=[90, 80, 70]
    ) == [0, 0, 0]


def test_correct_answer_case2():
    assert DailyTemperaturesSolution().daily_temperatures(
        temperatures=[70, 80, 90]
    ) == [1, 1, 0]


def test_correct_answer_case3():
    assert DailyTemperaturesSolution().daily_temperatures(
        temperatures=[70, 70, 70]
    ) == [0, 0, 0]


def test_correct_answer_stack_hashmap():
    assert DailyTemperaturesSolution().daily_temperatures_stack_hashmap(
        temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]


def test_correct_answer_case1_stack_hashmap():
    assert DailyTemperaturesSolution().daily_temperatures_stack_hashmap(
        temperatures=[90, 80, 70]
    ) == [0, 0, 0]


def test_correct_answer_case2_stack_hashmap():
    assert DailyTemperaturesSolution().daily_temperatures_stack_hashmap(
        temperatures=[70, 80, 90]
    ) == [1, 1, 0]


def test_correct_answer_case3_stack_hashmap():
    assert DailyTemperaturesSolution().daily_temperatures_stack_hashmap(
        temperatures=[70, 70, 70]
    ) == [0, 0, 0]


def test_correct_answer_case4_stack_hashmap():
    assert DailyTemperaturesSolution().daily_temperatures_stack_hashmap(
        temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    ) == [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]


def test_correct_answer_stack():
    assert DailyTemperaturesSolution().daily_temperatures_stack(
        temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
    ) == [1, 1, 4, 2, 1, 1, 0, 0]
