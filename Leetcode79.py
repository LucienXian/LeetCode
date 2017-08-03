class Solution(object):
    def exist(self, board, word):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.dfs(i, j, word, board):
                    return True
        return False
            
    
    def dfs(self, i, j, word, board):
        if not word:
            return True
        
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        
        temp = board[i][j]
        
        board[i][j] = '#'
        
        res = self.dfs(i+1, j, word[1:], board) or self.dfs(i-1, j, word[1:], board) \
        or self.dfs(i, j+1, word[1:], board) or self.dfs(i, j-1, word[1:], board)
        
        board[i][j] = temp
        
        return res