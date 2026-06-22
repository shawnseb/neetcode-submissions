class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min =  101
        best = 0
        for i in prices:
            if best < (i - min) :
                best = i - min
            if i < min:
                min  = i
        return best

        