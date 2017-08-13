class Solution(object):
    def search(self, nums, target):
        start, end = 0, len(nums)-1
        if end < 0:
            return -1
        while start < end:
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if  nums[mid] > target >= nums[start]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[end] >= target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        if nums[start] == target:
            return start
        else:
            return -1