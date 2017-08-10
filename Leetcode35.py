class Solution(object):
    def searchInsert(self, nums, target):
        i = 0
        if nums[0] >= target:
            return 0
        while i < len(nums):
            if nums[i] >= target and nums[i-1] < target:
                return i
            i += 1
        return i