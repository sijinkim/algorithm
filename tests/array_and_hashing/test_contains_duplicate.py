from src.array_and_hashing import ContainsDuplicateSolution


def test_can_check_without_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = ContainsDuplicateSolution(nums=nums)

    assert solution.duplicate_check() == False


def test_can_check_with_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    solution = ContainsDuplicateSolution(nums=nums)

    assert solution.duplicate_check() == True


def test_can_check_faster_without_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = ContainsDuplicateSolution(nums=nums)

    assert solution.duplicate_check_faster() == False


def test_can_check_faster_with_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    solution = ContainsDuplicateSolution(nums=nums)

    assert solution.duplicate_check_faster() == True


def test_can_check_more_faster_without_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = ContainsDuplicateSolution(nums=nums)

    assert solution.duplicate_check_more_faster() == False


def test_can_check_more_faster_with_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    solution = ContainsDuplicateSolution(nums=nums)

    assert solution.duplicate_check_more_faster() == True
