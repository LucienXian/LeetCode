class Solution(object):
    def findUnsortedSubarray(self, nums):
        start, end = -1, -2
        l, s = nums[0], nums[len(nums)-1]
        for i in range(1, len(nums)):
            l = max(l, nums[i])
            s = min(s, nums[len(nums)-i-1])
            if nums[i]<l:
                end = i
            if nums[len(nums)-i-1]>s:
                start = len(nums)-i-1
        return end-start+1