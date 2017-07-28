class Solution(object):
    def getRow(self, rowIndex):
        numRows = rowIndex+1
        res = [[1],[1,1]]
        if numRows == 0:
            return []
        elif numRows == 1:
            return [1]
        elif numRows == 2:
            return [1,1]
        else:
            for i in range(2, numRows):
                temp = []
                for j in range(i-1):
                    temp.append(sum(res[-1][j:j+2]))
                res.append([1]+temp+[1])
        res1 = res[rowIndex]
        return res1