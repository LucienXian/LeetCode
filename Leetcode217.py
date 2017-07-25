class Solution(object):
    def containsDuplicate(self, nums):
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            dict[nums[i]] = i
        return False