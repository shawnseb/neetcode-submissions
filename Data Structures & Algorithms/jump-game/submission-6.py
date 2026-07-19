class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.impossible = set()
        return self.jumpHelp(nums, 0) == 1
        
    def jumpHelp(self, nums: List[int], index: int) -> int:
        print(index)
        if index > len(nums):
            return 0
        if index == len(nums) - 1:
            return 1
        if index in self.impossible:
            return 0
        actions = nums[index]
        if actions == 0:
            self.impossible.add(index)
        sum = 0
        feasible = 0
        if (index + actions) >= len(nums):
            feasible = len(nums) - index -1
        else:
            feasible = actions
        for i in range(feasible, 0, -1):
            sum = sum + self.jumpHelp(nums, index + i)
            if sum == 1:
                return 1
        if sum == 0:
            self.impossible.add(index)
            return 0
        return 1


        
        