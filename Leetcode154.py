class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums)-1
        while low<high:
            if nums[low]<nums[high]:
                return nums[low]
            mid = (low+high)//2
            if nums[mid]>nums[high]:
                low = mid+1
            elif nums[mid]<nums[high]:
                high = mid
            else:
                high -= 1
        return nums[low]