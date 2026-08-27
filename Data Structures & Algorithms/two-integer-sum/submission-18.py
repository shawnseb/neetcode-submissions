class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        world = dict()
        index = 0
        for i in nums:
            
            if target - i in world:
                return [world[target-i], index]
            world[i] = index
            index += 1
        return []
        
        




        