import pytest

from src.stack import MinStack


@pytest.fixture
def init_stack() -> MinStack:
    stack_obj = MinStack()
    stack_obj.push(2)
    stack_obj.push(0)
    stack_obj.push(3)
    stack_obj.push(0)

    return stack_obj


def test_can_push(init_stack):
    init_stack.push(5)
    assert init_stack.stack == [{None: None}, {2: 2}, {0: 0}, {3: 0}, {0: 0}, {5: 0}]


def test_can_pop(init_stack):
    init_stack.pop()
    assert init_stack.stack == [{None: None}, {2: 2}, {0: 0}, {3: 0}]


def test_can_top(init_stack):
    assert init_stack.top() == 0


def test_can_get_min(init_stack):
    assert init_stack.get_min() == 0
