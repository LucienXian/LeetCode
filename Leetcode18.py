class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        self.find(nums, target, 4, [], res)
        return res
        
        
    def find(self, nums, target, N, path, res):
        if len(nums) < N or N < 2: return
        if N == 2:
            lo, hi = 0, len(nums)-1
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    res.append(path + [nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1
        else:
            for i in range(len(nums)-N+1):
                if target < nums[i]*N or target > nums[-1]*N:
                    return
                if i == 0 or nums[i] != nums[i-1]:
                    self.find(nums[i+1:], target-nums[i], N-1, path+[nums[i]], res)