from src.array_and_hashing import ContainsDuplicateSolution


def can_check_without_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    solution = ContainsDuplicateSolution(nums)

    assert solution.duplicate_check() == False


def can_check_with_duplicate_numbers():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
    solution = ContainsDuplicateSolution(nums)

    assert solution.duplicate_check() == True
