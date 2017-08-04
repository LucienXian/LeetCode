class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + (cols-1) * [0]
        for row in range(rows):
            for col in range(cols):
                if obstacleGrid[row][col]:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col-1]
        return dp[cols-1]