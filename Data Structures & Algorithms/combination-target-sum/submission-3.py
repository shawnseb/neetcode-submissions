class Solution:
    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.answer=[]
        self.help(nums, target, [], 0, 0)
        return self.answer
        
    def help(self, nums: List[int], target: int, current: List[int], index: int, sum: int):
        if index == len(nums):
            return
        if sum == target:
            if not current in self.answer:
                self.answer.append(current.copy())
                return
        if sum>target:
            return
        if sum < target:
            self.help(nums, target, current, index+1, sum)
            current.append(nums[index])
            sum = sum + nums[index]
            self.help(nums, target, current, index, sum)
            current.pop()
        return


        