class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxim = -1
        for i in range(length):
            if (heights[i] * (length-1-i)) < maxim:
                continue
            for j in range (i+1, length):
                var = (j-i)*min(heights[i],heights[j])
                if var > maxim:
                    maxim = var
        return maxim; 


