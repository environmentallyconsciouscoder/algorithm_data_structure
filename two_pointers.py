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

def check_for_target(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        # the current sum equals the target
        if curr == target:
            return True

        if curr > target:
            right -= 1
        else:
            left += 1

    return False

#this is given that the array is sorted
print("check_for_target",check_for_target([1,2,4,6,8,9,14,15], 13))

def combine(arr1: list[int], arr2: list[int]) -> list[int]:
    ans = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        #if the selected value in arr1 is less than arr2
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    # i think this is when you reach the end of one of the arrays
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1

    while j < len(arr2):
        ans.append(arr2[j])
        j += 1

    return ans