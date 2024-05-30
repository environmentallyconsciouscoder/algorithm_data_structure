# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverseString(self, s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        new_right = s[left]
        s[left] = s[right]
        s[right] = new_right
        left += 1
        right -= 1

# https://leetcode.com/problems/reverse-string/description/