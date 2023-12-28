import pytest

from src.basics import DynamicArray


@pytest.fixture
def sample_dynamic_array() -> DynamicArray:
    sample_array = DynamicArray(3)
    sample_array.pushback(1)
    sample_array.pushback(2)
    return sample_array


def test_dynamic_array_init_value_error():
    with pytest.raises(ValueError) as excinfo:
        DynamicArray(0)
    assert str(excinfo.value) == "Array capacity must be greater than 0."


def test_get_value(sample_dynamic_array):
    sample_array = sample_dynamic_array
    result: list = [sample_array.get(0), sample_array.get(1)]

    assert result == [1, 2]


def test_get_error_with_empty_array():
    sample_array = DynamicArray(1)

    with pytest.raises(IndexError) as excinfo:
        sample_array.get(0)
    assert str(excinfo.value) == "The array is empty."


def test_get_index_error_greater_than_size(sample_dynamic_array):
    sample_array = sample_dynamic_array

    with pytest.raises(IndexError) as excinfo:
        sample_array.get(2)
    assert (
        str(excinfo.value)
        == "The index is greater than the number of elements in the array."
    )


def test_get_index_error_less_than_zero(sample_dynamic_array):
    sample_array = sample_dynamic_array

    with pytest.raises(IndexError) as excinfo:
        sample_array.get(-2)
    assert str(excinfo.value) == "The index is less than 0."


def test_set_value(sample_dynamic_array):
    sample_array = sample_dynamic_array
    sample_array.set_new_value(0, 3)
    sample_array.set_new_value(1, 4)

    assert sample_array._array == [3, 4]


def test_set_index_error_greater_than_size(sample_dynamic_array):
    sample_array = sample_dynamic_array

    with pytest.raises(IndexError) as excinfo:
        sample_array.set_new_value(3, 3)
    assert (
        str(excinfo.value)
        == "The index is greater than the number of elements in the array."
    )


def test_set_index_error_less_than_zero(sample_dynamic_array):
    sample_array = sample_dynamic_array

    with pytest.raises(IndexError) as excinfo:
        sample_array.set_new_value(-3, 3)
    assert str(excinfo.value) == "The index is less than 0."


def test_can_pushback(sample_dynamic_array):
    sample_array = sample_dynamic_array

    sample_array.pushback(5)

    assert sample_array._array == [1, 2, 5]


def test_can_popback(sample_dynamic_array):
    sample_array = sample_dynamic_array

    assert sample_array.popback() == 2


def test_popback_error_with_empty_list():
    sample_array = DynamicArray(5)

    with pytest.raises(IndexError) as excinfo:
        sample_array.popback()
    assert str(excinfo.value) == "The array is empty."


def test_can_resize(sample_dynamic_array):
    sample_array = sample_dynamic_array

    sample_array.resize()

    assert sample_array._capacity == 6


def test_can_resize_automatically(sample_dynamic_array):
    sample_array = sample_dynamic_array
    sample_array.pushback(3)
    sample_array.pushback(4)

    assert sample_array._capacity == 6


def test_can_get_size_of_array_elements(sample_dynamic_array):
    assert sample_dynamic_array.get_size() == 2


def test_can_get_capacity_of_array(sample_dynamic_array):
    assert sample_dynamic_array.get_capacity() == 3
