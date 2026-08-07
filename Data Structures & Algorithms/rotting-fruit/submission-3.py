import copy
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        def spreadDisease(lazy:List[List[int]]) -> int:
            changed = 0
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if lazy[row][col] == 2:
                        #top
                        if row - 1>-1:
                            if lazy[row - 1][col] == 1:
                                changed += 1
                                grid[row-1][col] = 2
                        #right
                        if col + 1<len(grid[0]):
                            if lazy[row][col + 1] == 1:
                                changed += 1
                                grid[row][col + 1] = 2
                        #bottom
                        if row + 1 < len(grid):
                            if lazy[row + 1][col] == 1:
                                changed += 1
                                grid[row+ 1][col] = 2
                        #left
                        if col - 1>-1:
                            if lazy[row][col - 1] == 1:
                                changed += 1
                                grid[row][col - 1] = 2
            print(lazy)
            print(grid)
            return changed
        def checkFresh() -> bool:
            for row in grid:
                for col in row:
                    if col == 1:
                        return False
            return True
                    
        changed = -1
        turns = 0
        while changed != 0:
            print("hey")
            if checkFresh():
                return turns
            grid_copy = copy.deepcopy(grid)
            changed = spreadDisease(grid_copy)
            turns += 1
            

        return -1


        