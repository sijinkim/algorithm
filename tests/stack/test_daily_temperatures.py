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
