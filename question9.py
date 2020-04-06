def is_palindrome(stri):
    if stri == stri[::-1]:
        return True
    return False

print(is_palindrome("abba"))
print(is_palindrome("abab"))
print(is_palindrome("abcba"))
print(is_palindrome("abcab"))
print(is_palindrome("a"))
print(is_palindrome(""))