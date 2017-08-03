class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        for row in xrange(len(matrix)):
            if len(matrix[0]) == 0: return False
            if matrix[row][0] == target:
                return True
            if matrix[row][0] > target:
                row -= 1
                for col in xrange(len(matrix[0])):
                    if matrix[row][col] == target:
                        return True
                return False
        row = len(matrix) - 1
        for col in xrange(len(matrix[0])):
            if matrix[row][col] == target:
                return True
        return False