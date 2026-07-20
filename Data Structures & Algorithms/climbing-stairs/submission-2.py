class Solution:
    def climbStairs(self, n: int) -> int:
        self.stairs = [0] * (n+1)
        self.stairs[n] = 1
        self.stairs[n-1] =1
        for i in range (n-2, -1, -1):
            self.stairs[i] = self.stairs[i+1] + self.stairs[i+2]
        return self.stairs[0]
        
    
        
        
        