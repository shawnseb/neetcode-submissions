class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        index = len(digits) -1
        while digits[index] == 9 and index >= 0:
            digits[index] = 0
            index -= 1
        
        if index == -1:
            return [1] + digits
        else:
            digits[index] += 1
            return digits
      

            
        