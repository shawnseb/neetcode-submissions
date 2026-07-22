class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        for i in range(0, len(nums)-1, 1):
            if nums[i] != target:
                if nums[i] > nums[i+1]:
                    start = i + 1
                    break
            else:
                return i
        print("hi")
        print(start)
        low = start
        high = len(nums) -1 + start
        print(high)
        while low <= high:
            mid = (low + high)//2
            midInd = mid%len(nums)
            print(midInd)
            if nums[midInd] > target:
                high = mid -1
            elif nums[midInd] < target:
                low = mid+1
            else:
                return midInd
        return -1


        