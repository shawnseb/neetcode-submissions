class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        world = set()
        for num in nums:
            if num in world:
                return num
            world.add(num)
        return -1
        