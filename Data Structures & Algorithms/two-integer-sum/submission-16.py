class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        i = 0
        for c in nums:
            if  c in map:
                if c+ c == target:
                    return [map[c], i]
            map[c]=i
            i = i + 1
        
        for c in map:
            if target - c in  map  and map[target-c] != map[c]:
                return [map[c], map[target-c]]




        