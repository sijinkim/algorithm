from src.stack import EvaluateReversePolishNotationSolution


def test_can_evaluate_answer():
    test_input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    assert EvaluateReversePolishNotationSolution().eval_rpn(tokens=test_input) == 22
