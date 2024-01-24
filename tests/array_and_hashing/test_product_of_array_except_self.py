import pytest

from src.array_and_hashing import ProductOfArrayExceptSelfSolution


@pytest.fixture
def nums():
    return [[1, 2, 3, 4], [-1, 1, 0, -3, 3]]


def test_can_product_except_self(nums):
    assert ProductOfArrayExceptSelfSolution(nums=nums[0]).product_except_self() == [
        24,
        12,
        8,
        6,
    ]


def test_can_product_except_self_with_zero_element(nums):
    assert ProductOfArrayExceptSelfSolution(nums=nums[1]).product_except_self() == [
        0,
        0,
        9,
        0,
        0,
    ]
