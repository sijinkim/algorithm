import pytest

from src.basics import LinkedList, Node


@pytest.fixture
def linked_list() -> LinkedList:
    sample_list = LinkedList()
    sample_list.insert_head(1)
    sample_list.insert_head(2)
    return sample_list


def tset_can_insert_head(linked_list):
    sample_list = linked_list
    sample_list.insert_head(3)

    assert sample_list.get_values() == [3, 2, 1]


def test_can_insert_tail(linked_list):
    sample_list = linked_list
    sample_list.insert_trail(3)

    assert sample_list.get_values() == [2, 1, 3]


def test_get_ith_value(linked_list):
    assert linked_list.get(0) == 2
    assert linked_list.get(1) == 1


def test_get_fail_with_out_of_bounds_index(linked_list):
    assert linked_list.get(2) == -1


def test_get_fail_with_negative_number_index(linked_list):
    with pytest.raises(ValueError) as excinfo:
        linked_list.get(-1)
    assert str(excinfo.value) == "Index must be greater than or equal to 0."


def test_remove_ith_node(linked_list):
    sample_list = linked_list
    return_value = sample_list.remove(0)

    assert sample_list.get_values() == [1]
    assert return_value == True


def test_remove_middle_node():
    sample_list = LinkedList()
    sample_list.insert_head(1)
    sample_list.insert_head(2)
    sample_list.insert_head(3)

    return_value = sample_list.remove(1)

    assert sample_list.get_values() == [3, 1]
    assert return_value == True


def test_remove_fail_with_out_of_bounds_index(linked_list):
    sample_list = linked_list
    return_value = sample_list.remove(2)

    assert sample_list.get_values() == [2, 1]
    assert return_value == False


def test_remove_fail_with_negative_number_index(linked_list):
    with pytest.raises(ValueError) as excinfo:
        linked_list.remove(-1)
    assert str(excinfo.value) == "Index must be greater than or equal to 0."


def test_get_values(linked_list):
    assert linked_list.get_values() == [2, 1]
