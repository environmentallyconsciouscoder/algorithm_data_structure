def check_if_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        #if the left and right pointer char
        # is not equal then escape
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print("check_if_palindrome",check_if_palindrome("racecar"))

