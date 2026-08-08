import heapq
import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)
        while(len(stones)>1):
            left = heapq.heappop(stones) * -1
            right = heapq.heappop(stones) * -1
            add = math.fabs(left - right)
            heapq.heappush(stones, -1 * add)
        if len(stones) > 0:
            return int(-1 * stones[0])
        else:
            return 0


        
        