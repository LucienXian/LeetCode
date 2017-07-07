class Solution(object):
    def arrayNesting(self, nums):
        res, visited = 0, [False]*len(nums)
        for i in range(0, len(nums)):
            count = 0
            temp = i
            while not visited[temp]:
                visited[temp] = True
                count = count+1
                temp = nums[temp]
            res = max(res, count)
        return res