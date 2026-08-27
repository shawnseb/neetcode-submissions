class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        world = set()
        for i in nums:
            if i in world:
                return True
            world.add(i)
        return False


        