import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        heap = []
        for elem in seen:
            heapq.heappush(heap, (-1* seen[elem], elem))
        answer = []
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer
            

        

        
            
        