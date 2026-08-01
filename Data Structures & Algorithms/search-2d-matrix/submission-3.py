class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        line = self.findRow(matrix, target)
        print(line)
        return self.findTarget(matrix[line], target)

    def findRow(self, matrix: List[List[int]], target)-> int:
        left = 0 
        right = len(matrix)-1
        middle = (left + right)//2
        while left<=right:
            if target >= matrix[middle][0] and middle+1 < len(matrix) and target < matrix[middle+1][0]:
                return middle
            elif target >= matrix[middle][0] and middle + 1== len(matrix):
                return middle
            elif target > matrix[middle][0]:
                left = middle +1
                middle = (left+ right)//2
            elif target<matrix[middle][0] and middle == 0:
                return -1
            else:
                right = middle -1
                middle = (left+ right)//2
        return -1
    def findTarget(self, line: List[int], target) -> bool:
        left = 0
        right = len(line)-1
        middle = (left+ right)//2
        while left<=right:
            if target==line[middle]:
                return True
            elif target>line[middle]:
                left = middle+1
                middle = (left+right)//2
            else:
                right = right - 1
                middle = (left+right)//2
        return False
            

                

        


        