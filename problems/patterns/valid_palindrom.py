def valid_palindrome(s: str):

    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


assert valid_palindrome("A man, a plan, a canal: Panama") is True
assert valid_palindrome("race a car") is False
assert valid_palindrome(" ") is True
assert valid_palindrome(".,") is True
print("All tests passed")
