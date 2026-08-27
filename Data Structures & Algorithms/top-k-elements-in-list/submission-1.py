import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        world = dict()
        for i in nums:
            if i in world:
                world[i] += 1
            else:
                world[i] = 1
        answer = []
        for i in world:
            heapq.heappush(answer, (-world[i], i))
        biganswer = []
        for i in range(k):
            result = heapq.heappop(answer)
            biganswer.append(result[1])
        return biganswer

        
            
        