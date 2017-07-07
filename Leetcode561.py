class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if i%2 == 0:
                count += nums[i]
        return count 