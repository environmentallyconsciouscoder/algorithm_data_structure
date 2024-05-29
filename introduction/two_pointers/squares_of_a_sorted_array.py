# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# https://leetcode.com/problems/squares-of-a-sorted-array/description/

def sortedSquares(nums: list[int]) -> list[int]:
    arr = [num * num for num in nums]
    arr.sort()
    return arr