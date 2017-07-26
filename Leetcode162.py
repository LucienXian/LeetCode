class Solution(object):
    def findPeakElement(self, nums):
        low, high = 0, len(nums)-1
        while low<high:
            mid = (low+high)//2
            if nums[mid+1]<nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                low = mid+1
            elif nums[mid-1]>nums[mid]:
                high = mid-1
        return low