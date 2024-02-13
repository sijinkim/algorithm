import pytest

from src.stack import GenerateParenthesesSolution


def test_correct_output():
    assert GenerateParenthesesSolution(n=3).generate_parenthesis() == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]


def test_one_pair_case():
    assert GenerateParenthesesSolution(n=1).generate_parenthesis() == ["()"]


def test_n_out_of_range_case():
    with pytest.raises(ValueError) as excinfo:
        GenerateParenthesesSolution(n=0).generate_parenthesis()
