class Solution(object):
    def subarraySum(self, nums, k):
        pre_sum = {0:1}
        get_sum, count = 0, 0
        for num in nums:
            get_sum += num
            count += pre_sum.get(get_sum-k, 0)
            pre_sum[get_sum] = pre_sum.get(get_sum, 0) + 1
        return count