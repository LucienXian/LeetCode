class Solution(object):
    def combinationSum3(self, k, n):
        if n>sum([i for i in range(1, 10)]):
            return []
        res = []
        self.compute(k, n, 1, [], res)
        return res
    def compute(self, k, n, ind, ele, res):
        if len(ele) == k and sum(ele) == n:
            res.append(list(ele))
            return
        if ind > 9 or len(ele) > k:
            return
        for i in range(ind, 10):
            ele.append(i)
            self.compute(k, n, i+1, ele, res)
            ele.pop()