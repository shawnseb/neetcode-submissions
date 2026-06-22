class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min =  101
        best = 0
        for i in prices:
            mark = i - min
            if best < mark :
                best = mark
            if i < min:
                min  = i
        return best

        