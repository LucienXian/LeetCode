class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i, v in enumerate(nums):
            if v in dict and i-dict[v]<=k:
                return True
            dict[v] = i
        return False