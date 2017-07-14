class Solution(object):
    def findDuplicate(self, nums):
        low, high = 1, len(nums)-1
        while low < high:
            count, mid = 0, (high+low)/2            
            for i in nums:
                if i <= mid:
                    count+=1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low