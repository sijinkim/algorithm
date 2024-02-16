from io import StringIO

import pytest

from src.study import firefly_solution, firefly_time_solution


@pytest.fixture
def sample_inputs():
    return StringIO("6 7\n1\n5\n3\n3\n5\n1\n")


def test_correct_answer(monkeypatch, capsys, sample_inputs):
    monkeypatch.setattr("sys.stdin", sample_inputs)
    firefly_solution()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "2 3\n"


def test_correct_answer_and_time(monkeypatch, capsys, sample_inputs):
    monkeypatch.setattr("sys.stdin", sample_inputs)
    firefly_time_solution()
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout == "2 3\n"
