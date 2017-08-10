class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, res, [])
        return res
    
    def dfs(self, nums, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] == nums[i-1] and i != index:
                continue
            self.dfs(nums, target-nums[i], i+1, res, path+[nums[i]])