class Solution(object):
    def sortColors(self, nums):
        i, j = 0, 0
        for k in xrange(len(nums)):
            temp = nums[k]
            nums[k] = 2
            if temp < 2:
                nums[j] = 1
                j += 1
            if temp == 0:
                nums[i] = 0
                i += 1