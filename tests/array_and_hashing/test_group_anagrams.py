from src.array_and_hashing import GroupAnagramsSolution

def test_can_check_group_anagrams():
    inputs = ["eat","tea","tan","ate","nat","bat"]
    
    assert GroupAnagramsSolution(strs = inputs) == [["bat"],["nat","tan"],["ate","eat","tea"]]

def test_can_check_empty_lists():
    inputs = [""]

    assert GroupAnagramsSolution(strs = inputs) == [[""]]

def test_can_check_single_element():
    inputs = ["a"]

    assert GroupAnagramsSolution(strs = inputs) == [["a"]]

def test_can_check_duplicate_elements():
    inputs = ["eat","tea","tan", "tea", "ant"]

    assert GroupAnagramsSolution(strs = inputs) == [["eat", "tea", "tea"], ["tan", "ant"]]