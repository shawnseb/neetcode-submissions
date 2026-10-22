class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, num in enumerate(nums):
            needle = target - num
            if needle in seen:
                return [seen[needle], index]
            seen[num] = index
        return [-1, -1]


        