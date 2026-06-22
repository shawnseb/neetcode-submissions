class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set();
        for n in nums:
            if n in seen_numbers:
                return True
            seen_numbers.add(n)

        return False
        



        