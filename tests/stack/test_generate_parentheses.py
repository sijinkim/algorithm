from src.stack import GenerateParenthesesSolution
import pytest

def test_correct_output():
    assert GenerateParenthesesSolution.generate_parenthesis(n=3) == ["((()))","(()())","(())()","()(())","()()()"]

def test_one_pair_case():
    assert GenerateParenthesesSolution.generate_parenthesis(n=1) == ["()"]

def test_n_out_of_range_case():
    with pytest.raises(ValueError) as excinfo:
        GenerateParenthesesSolution.generate_parenthesis(n=0)
    assert str(excinfo.value) == "1 <= n <= 8"
