class Solution(object):
    def searchRange(self, nums, target):
        def find(target):
            start, end = 0, len(nums)
            while start < end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid
            return start
        low = find(target)
        return [low, find(target+1)-1] if target in nums[low:low+1] else [-1, -1]# if nums == [], nums[low:low+1] return []