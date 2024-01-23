import pytest

from src.array_and_hashing import TopKFrequentElementsSolution


@pytest.fixture
def input_nums():
    return [1, 1, 1, 2, 2, 3]


def test_can_check_counter(input_nums):
    assert TopKFrequentElementsSolution(nums=input_nums, k=2).top_k_frequent() == [1, 2]
