from io import StringIO

from src.study import range_sum_query_solution

sample_inputs = StringIO("5 3\n5 4 3 2 1\n1 3\n2 4\n5 5\n")


def test_correct_answer(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", sample_inputs)
    range_sum_query_solution()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "12\n9\n1\n"
