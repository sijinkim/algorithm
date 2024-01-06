from src.array_and_hashing import ValidAnagramSolution

def test_true_case():
    s = "anagram"
    t = "nagram"

    assert ValidAnagramSolution(s, t).isAnagram() == True

def test_false_case():
    s = "anagram"
    t = "antaram"

    assert ValidAnagramSolution(s, t).isAnagram() == False
