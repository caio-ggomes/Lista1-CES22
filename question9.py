from test import test

def is_palindrome(stri):
    if stri == stri[::-1]:
        return True
    return False


def test_suite():
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))

test_suite()