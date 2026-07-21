class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
         world = dict()
         startIndices = []
         if not board:
            return False
         self.width = len(board)
         self.length = len(board[0])
         for i in range(len(board)):
            for j in range(len(board[i])):
                print(board[i][j])
                print(i * len(board[0]) + j + 1)
                world[i * len(board[0]) + j + 1] = board[i][j]
                if word[0] == board[i][j]:
                    startIndices.append(i * len(board[0]) + j + 1)
         print(world)
         for i in startIndices:
            if self.help(world, word, i, 0, set()):
                return True
         return False


    def help(self, board: dict(), word: str, position: int, index:int, current: set()) -> bool:
        if index == len(word):
            return True
        if position in board and board[position] == word[index] and position not in current:
            print(board[position])
            current.add(position)
            if ((position + 1) % self.length) == 1:
                bole = self.help(board, word, position - 1, index + 1, current) or self.help(board, word, position + self.length, index + 1, current) or self.help(board, word, position - self.length, index + 1, current)
            elif (position -1) % self.length == 0:
                bole = self.help(board, word, position +1, index + 1, current) or self.help(board, word, position + self.length, index + 1, current) or self.help(board, word, position - self.length, index + 1, current)
            else:
                bole = self.help(board, word, position +1, index + 1, current) or self.help(board, word, position -1, index + 1, current) or self.help(board, word, position + self.length, index + 1, current) or self.help(board, word, position - self.length, index + 1, current)

            current.remove(position)
            return bole
        return False

        