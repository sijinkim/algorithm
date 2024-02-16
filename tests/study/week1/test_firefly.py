from io import StringIO

from src.study import firefly_solution

sample_inputs = StringIO("6 7\n1\n5\n3\n3\n5\n1\n")


def test_correct_answer(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", sample_inputs)
    firefly_solution()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "2 3\n"
