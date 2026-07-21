class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                return max(nums[0], num[1])
        n = len(nums)
        answer = [0] * n
        answer[n-1] = nums[n-1]
        answer[n-2] = max(nums[n-1], nums[n-2])
        for i in range (len(nums)-3, -1, -1):
            if (nums[i] + answer[i+2]) > answer[i+1]:
                answer[i] = nums[i] + answer[i+2]
            else:
                answer[i] = answer[i+1]

        return answer[0]
            
