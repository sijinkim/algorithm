from src.array_and_hashing import GroupAnagramsSolution


def test_can_check_group_anagrams():
    inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert sorted(GroupAnagramsSolution(strs=inputs).group_anagrams()) == sorted(
        [
            ["bat"],
            ["nat", "tan"],
            ["ate", "eat", "tea"],
        ]
    )


def test_can_check_empty_lists():
    inputs = [""]

    assert GroupAnagramsSolution(strs=inputs).group_anagrams() == [[""]]


def test_can_check_single_element():
    inputs = ["a"]

    assert GroupAnagramsSolution(strs=inputs).group_anagrams() == [["a"]]


def test_can_check_duplicate_elements():
    inputs = ["eat", "tea", "tan", "tea", "ant"]

    assert sorted(GroupAnagramsSolution(strs=inputs).group_anagrams()) == sorted(
        [
            ["eat", "tea", "tea"],
            ["ant", "tan"],
        ]
    )


def test_can_check_same_length_strs():
    inputs = ["dddg", "gggd"]

    assert sorted(GroupAnagramsSolution(strs=inputs).group_anagrams()) == sorted(
        [["dddg"], ["gggd"]]
    )
