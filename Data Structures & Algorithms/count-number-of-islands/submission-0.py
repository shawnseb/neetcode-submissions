class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.map = dict()
        self.ans = set()
        sum = 0
        j=0
        
        for lisp in range (len(grid)):
            for i in range (len(grid[lisp])):
                if grid[lisp][i] == "1":
                    self.help(grid, lisp, i, lisp*len(grid) + i)
        return len(self.ans)

        
    
    def help(self, grid: List[List[str]], row: int, col: int, island: int):
        if row*len(grid[0])+col in self.map:
            return
        self.map[row*len(grid[0])+col] = island
        
        self.ans.add(island)
        #up
        if row > 0 and grid[row-1][col] == "1":
            self.help(grid, row-1, col, island)
        #left
        if col > 0 and grid[row][col-1] == "1":
            self.help(grid, row, col-1, island)
        #right
        if col+1 < len(grid[0]) and grid[row][col+1] == "1":
            self.help(grid, row, col+1, island)
        #down
        if row+1 < len(grid) and grid[row+1][col] == "1":
            self.help(grid, row+1, col, island)
        return 

