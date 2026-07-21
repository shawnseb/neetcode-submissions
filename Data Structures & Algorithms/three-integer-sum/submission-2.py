class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        world = dict()
        answer = set()
        k = 0
        for i in nums:
            if i not in world:
                world[i]= k

            k = k+ 1

        for i in range (len(nums)):
            for j in range (i, len(nums), 1):
                if i == j:
                    continue
                else:
                    num = (nums[i] + nums[j]) * -1
                    if num in world and world[num] != i and world[num]!=j:
                        triplet = [nums[i], nums[j], num]
                        triplet.sort()
                        answer.add(tuple(triplet))
    
        return [list(t) for t in answer]

