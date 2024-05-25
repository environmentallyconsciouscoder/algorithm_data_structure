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