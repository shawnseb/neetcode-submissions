class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        maxim = -1
        while(i<j):
            var = min(heights[i], heights[j]) * (j-i) 
            if maxim < var:
                maxim = var

            if heights[i] < heights[j] :
                i=i+1
            elif heights[i] == heights[j]:
                i=i+1
                j=j-1
            else:
                j=j-1

        return maxim




