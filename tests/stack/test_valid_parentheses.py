import pytest

from src.stack import ValidParenthesesSolution


@pytest.fixture
def inputs() -> list[str]:
    return ["()", "()[]{}", "()]", "{{}}]", "()[", "{[{()}}"]


def test_can_check_valid(inputs):
    assert ValidParenthesesSolution(s=inputs[0]).is_valid() == True
    assert ValidParenthesesSolution(s=inputs[1]).is_valid() == True


def test_can_check_not_opened(inputs):
    assert ValidParenthesesSolution(s=inputs[2]).is_valid() == False
    assert ValidParenthesesSolution(s=inputs[3]).is_valid() == False


def test_can_check_not_closed(inputs):
    assert ValidParenthesesSolution(s=inputs[4]).is_valid_with_stack() == False
    assert ValidParenthesesSolution(s=inputs[5]).is_valid_with_stack() == False


def test_can_check_valid_with_stack(inputs):
    assert ValidParenthesesSolution(s=inputs[0]).is_valid_with_stack() == True
    assert ValidParenthesesSolution(s=inputs[1]).is_valid_with_stack() == True


def test_can_check_not_opened_with_stack(inputs):
    assert ValidParenthesesSolution(s=inputs[2]).is_valid_with_stack() == False
    assert ValidParenthesesSolution(s=inputs[3]).is_valid_with_stack() == False


def test_can_check_not_closed_with_stack(inputs):
    assert ValidParenthesesSolution(s=inputs[4]).is_valid_with_stack() == False
    assert ValidParenthesesSolution(s=inputs[5]).is_valid_with_stack() == False
