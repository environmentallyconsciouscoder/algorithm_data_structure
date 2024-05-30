def find_length(nums: list[int], k: int) -> int:
    left = curr = ans = 0

    for right in range(len(nums)):
        curr += nums[right]
        #we keeping adding until the sum (curr)is greater than k
        while curr > k:
            #you remove element from the left
            curr -= nums[left]
            left += 1

        ans = max(ans, right - left + 1)

    return ans

print(find_length([3,1,2,7,4,2,1,1,5], 8))

def find_length_two(s: str) -> int:
    left = curr = ans = 0
    for right in range(len(s)):
        if s[right] == "0":
            curr += 1

        while curr > 1:
            if s[left] == "0":
                curr -= 1
            left += 1

        ans = max(ans, right - left + 1)

    return ans

print(find_length_two("11001011"))

def numSubarrayProductLessThank(nums: list[int], k: int) -> int:
    if k <= 1:
        return 0

    ans = left = 0
    curr = 1

    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1

        ans += right - left + 1

    return ans

print(numSubarrayProductLessThank([10,5,2,6], 100))

def find_best_subarray(nums: list[int], k: int):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        ans = max(ans, curr)
    return ans

print(find_best_subarray([3,-1,4,12,-8,5,6], 4))