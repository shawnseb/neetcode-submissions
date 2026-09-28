import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        heap = []
        for elem in counts:
            if len(heap) == k and counts[elem] > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (counts[elem], elem))
            elif len(heap) < k:
                heapq.heappush(heap, (counts[elem], elem))
        
        heap.sort(reverse = True)
        answer = []
        for i in heap:
            answer.append(i[1])
        return answer
        

            

        

        
            
        