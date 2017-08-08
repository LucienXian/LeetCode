 class Solution(object):
    def maxSubArray(self, nums):
        length = len(nums)
        dp = [0]*length
        res = dp[0] = nums[0]
        for i in range(1, length):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
            res = max(dp[i], res)
        return res