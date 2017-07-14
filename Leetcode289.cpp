class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int row = board.size();
        int col = board[0].size();
        for(int i=0; i<row; i++)
            for (int j=0; j<col; j++){
                int live = 0;
                for (int k=max(0, i-1); k<min(row, i+2); k++)
                    for (int n=max(0, j-1); n<min(col, j+2); n++)
                        live += board[k][n]&1;
                if(live==3 || live-board[i][j]==3) board[i][j]|=2;
            }
        for(int i=0; i<row; i++)
            for (int j=0; j<col; j++)
                board[i][j]>>=1;
    }
};