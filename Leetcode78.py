class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in xrange(len(nums)):
            for j in xrange(len(res)):
                res.append(res[j]+[nums[i]])
        return res