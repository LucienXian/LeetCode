class Solution(object):
    def combinationSum(self, candidates, target):
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
        else:
            for i in range(index, len(nums)):
                self.dfs(nums, target-nums[i], i, res, path+[nums[i]])