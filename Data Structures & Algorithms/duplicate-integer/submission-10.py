class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = set()
        for elem in nums:
            if elem in dictionary:
                return True
            else:
                dictionary.add(elem)
        return False


        