class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if nums[0] <= nums[length-1]:
            return nums[0]
        left = 0
        right =  length-1
        mid = right // 2
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]



            

            
    
        
        