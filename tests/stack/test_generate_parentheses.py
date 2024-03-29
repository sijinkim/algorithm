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


def test_correct_output_with_dfs():
    assert GenerateParenthesesSolution(n=3).generate_parenthesis_dfs() == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]


def test_one_pair_case_with_dfs():
    assert GenerateParenthesesSolution(n=1).generate_parenthesis_dfs() == ["()"]


def test_n_out_of_range_case_with_dfs():
    with pytest.raises(ValueError) as excinfo:
        GenerateParenthesesSolution(n=0).generate_parenthesis_dfs()
