from src.study import cache_solution


def test_can_get_correct_answer():
    cache_size = 3
    cities = [
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
        "Jeju",
        "Pangyo",
        "Seoul",
        "NewYork",
        "LA",
    ]
    assert cache_solution(cache_size, cities) == 50
