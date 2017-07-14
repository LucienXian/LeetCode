class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        count = 0
        for i in nums:
            if i!=count:
                return count
            count += 1
        return i+1