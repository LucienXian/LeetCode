class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        for i in range(2, len(nums)):
            f = 0
            l = i-1
            while (l>f):
                if nums[f] + nums[l] > nums[i]:
                    res = res + l-f
                    l -= 1
                else:
                    f += 1
        return res