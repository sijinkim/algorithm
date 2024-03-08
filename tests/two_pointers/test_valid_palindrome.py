from src.two_pointers.valid_palindrome import ValidPalindromeSolution


def test_can_check_palindrome():
    assert (
        ValidPalindromeSolution().is_palindrome(s="A man, a plan, a canal: Panama")
        == True
    )


def test_can_check_non_palindrome():
    assert ValidPalindromeSolution().is_palindrome(s="race a car") == False


def test_can_check_empty():
    assert ValidPalindromeSolution().is_palindrome(s=" ") == True


def test_can_check_palindrome_fast():
    assert (
        ValidPalindromeSolution().is_palindrome_fast(s="A man, a plan, a canal: Panama")
        == True
    )
