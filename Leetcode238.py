class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        count = 1
        for num in nums:
            output.append(count)
            count *= num
        count = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= count
            count *= nums[i]
        return output