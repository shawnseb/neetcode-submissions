class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        auto init = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
        int rows[9] = {0};
        int cols[9] = {0};
        int boxes[9] = {0};

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') continue;
                int bit = 1 << (c - '1');
                int b = (i / 3) * 3 + (j / 3);
                if ((rows[i] & bit) || (cols[j] & bit) || (boxes[b] & bit))
                    return false;
                rows[i]  |= bit;
                cols[j]  |= bit;
                boxes[b] |= bit;
            }
        }
        return true;
    }
};