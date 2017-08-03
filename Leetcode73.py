class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        col0 = 1
        for row in range(rows):
            if matrix[row][0] == 0: col0 = 0
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0
                    
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, 0, -1):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
            if col0 == 0: matrix[row][0] = 0