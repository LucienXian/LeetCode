class Solution(object):
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        for row in range(1, rows):
            grid[row][0] += grid[row-1][0]
        for col in range(1, cols):
            grid[0][col] += grid[0][col-1]
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]