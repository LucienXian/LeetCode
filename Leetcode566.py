class Solution(object):
    def matrixReshape(self, nums, r, c):
        res = [[None] * c for _ in xrange(r)]
        m, n = len(nums), len(nums[0])
        if m*n != r*c:
            return nums
        for i in range(0, r*c):
            res[i/c][i%c] = nums[i/n][i%n]
        return res