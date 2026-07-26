class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        s = s.lower()
        while left <= right:
            # To skip non-alphanumeric characters on the left
            while left < right and not s[left].isalnum():
                left += 1

# To skip non-alphanumeric characters on the right
            while left < right and not s[right].isalnum():
                right -= 1
            if left > right:
                return False
            if s[left] != s[right]:
                print(s[left])
                print(s[right])
                return False
            left = left+1
            right = right -1
        return True

        