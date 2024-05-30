def runningSum(self, nums: list[int]) -> list[int]:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        print("i", i)
        print("prefix", prefix)
        print("this will get last element on list", prefix[-1])
        prefix.append(nums[i] + prefix[-1])
    return prefix