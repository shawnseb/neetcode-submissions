class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        maxim = -1
        for i in range(length):
            if (heights[i] * (length-1-i)) < maxim:
                continue
            for j in range (i+1, length):
                if (j-i)*min(heights[i],heights[j])> maxim:
                    maxim = (j-i)*min(heights[i],heights[j])
                    print(i, j, maxim)
                    

        return maxim; 


