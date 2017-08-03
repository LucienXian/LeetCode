class Solution(object):
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[high]:
                if nums[mid]>target and nums[low]<=target:
                    high = mid
                else:
                    low = mid + 1
            elif nums[mid] < nums[high]:
                if nums[mid]<target and nums[high] >= target:
                    low = mid+1
                else:
                    high = mid
            else:
                high -= 1
        return low < len(nums) and nums[low] == target