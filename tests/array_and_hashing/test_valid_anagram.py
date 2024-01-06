import pytest

from src.array_and_hashing import ValidAnagramSolution


def test_true_case():
    s = "anagram"
    t = "nagaram"

    assert ValidAnagramSolution(s=s, t=t).is_anagram() == True


def test_false_case():
    s = "aacc"
    t = "ccac"

    assert ValidAnagramSolution(s=s, t=t).is_anagram() == False


def test_length_checker():
    s = ""
    t = "ksk"

    with pytest.raises(ValueError) as excinfo:
        ValidAnagramSolution(s=s, t=t)


def test_true_case_faster():
    s = "anagram"
    t = "nagaram"

    assert ValidAnagramSolution(s=s, t=t).is_anagram_faster() == True


def test_false_case_faster():
    s = "aacc"
    t = "ccac"

    assert ValidAnagramSolution(s=s, t=t).is_anagram_faster() == False
