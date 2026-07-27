class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        if not nums:
            nums = []
        for q in range (len(nums)):
            nums[q] = -1 * nums[q]
        heapq.heapify(nums)
        self.records = nums
        self.index = k
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.records,-1 * val)
        copy = []
        if self.index > len(self.records):
            return -1
        for i in range(self.index):
            copy.append(heapq.heappop(self.records))
        answer = copy[-1]
        for i in copy:
            heapq.heappush(self.records, i)
        return answer * -1

        
