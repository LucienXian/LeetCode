class Solution(object):
    def maxProduct(self, nums):
        res = min_e = max_e = nums[0]
        for i in range(1, len(nums)):
            temp = max_e
            max_e = max(max(nums[i]*min_e, nums[i]*temp), nums[i])
            min_e = min(min(nums[i]*min_e, nums[i]*temp), nums[i])
            res = max(max_e, res)
        return res