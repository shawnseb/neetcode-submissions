class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        total = 0
        max = -1000
        while left< len(nums) and right < len(nums):
            if left == right:
                print(total)
                print(left)
                print(right)
                total = nums[left]
                right = right + 1
                if max < total:
                    max  = total
                if total < 0:
                    left = left + 1
            elif left < right:
                total = total + nums[right]
                if max < total:
                    max  = total
                if total < 0:
                    left = right + 1
                    right = right +1
                else:
                    right = right + 1
        return max