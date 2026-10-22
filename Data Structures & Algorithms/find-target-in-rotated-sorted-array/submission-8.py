import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchEdge(left, right):
            if nums[left] < nums[right]:
                return left
            if right - left == 1:
                return right
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                return searchEdge(middle, right)
            if nums[left] > nums[middle-1]:
                return searchEdge(left, middle-1)
            return middle

        split = searchEdge(0, len(nums)-1)
        print(split)
        


        actual = nums[split:len(nums)]
        rem = nums[0:split]
        for num in rem:
            actual.append(num)
        print(actual)
        def binary_search_left(arr, val):
            """Finds the FIRST occurrence index of val, or -1 if missing."""
            idx = bisect.bisect_left(arr, val)
            # 1. Check if index is within the list boundaries
            # 2. Check if the element at that index is actually our target
            if idx < len(arr) and arr[idx] == val:
                return idx
            return -1
        if binary_search_left(actual, target) == -1:
            return -1
        return (binary_search_left(actual, target) + split) % len(nums)



        