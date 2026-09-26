class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, elem in enumerate(nums):
            if target - elem in seen:
                return [seen[target-elem], i]
            else:
                seen[elem] = i
        return []
            
            

        
        




        