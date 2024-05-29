def findMaxAverage(self, nums: list[int], k: int) -> float:
    curr = 0

    #you only need to add the first 4
    for i in range(k):
        curr += nums[i]

    ans = curr /k
    for i in range(k, len(nums)):

        #the rest would be loss and gain
        curr += nums[i] - nums[i - k]

        #you compare the curr with prev each time to find the highest
        ans = max(ans, curr /k)
    return ans