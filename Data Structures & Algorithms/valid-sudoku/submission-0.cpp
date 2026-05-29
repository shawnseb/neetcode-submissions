class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Check rows
        for(short i = 0; i < 9; i++)
        {
            unordered_set<char> seen;
            for(short j = 0; j < 9; j++)
            {
                if(board[i][j] == '.') continue;
                if(!(seen.find(board[i][j]) == seen.end()))
                    return false;
                seen.insert(board[i][j]);
            }
        }

        // Check columns
        for(short j = 0; j < 9; j++)
        {
            unordered_set<char> seen;
            for(short i = 0; i < 9; i++)
            {
                if(board[i][j] == '.') continue;
                if(!(seen.find(board[i][j]) == seen.end()))
                    return false;
                seen.insert(board[i][j]);
            }
        }

        return isValidBox(board, 0, 0) && isValidBox(board, 3, 0) && isValidBox(board, 0, 3) &&
               isValidBox(board, 6, 0) && isValidBox(board, 0, 6) && isValidBox(board, 3, 3) &&
               isValidBox(board, 6, 6) && isValidBox(board, 3, 6) && isValidBox(board, 6, 3);
    }

    bool isValidBox(vector<vector<char>>& board, short i, short j){
        unordered_set<char> seen;
        short si = i;
        short sj = j;
        for(; i < si + 3; i++)
        {
            for(short jj = sj; jj < sj + 3; jj++)
            {
                if(board[i][jj] == '.') continue;
                if(!(seen.find(board[i][jj]) == seen.end()))
                    return false;
                seen.insert(board[i][jj]);
            }
        }
        return true;
    }
};