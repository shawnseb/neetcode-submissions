class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        current = set()
        maxCount= 0
        while left <= len(s) - maxCount and right < len(s):
            if left == right:
                current.add(s[right])
                if maxCount < 1:
                    maxCount = 1
                right = right + 1
            elif left < right and right < len(s):
                
                if s[right] in current:
                    while left < right:
                        if s[left] == s[right]:
                            left = left+1
                            right = right + 1
                            break
                        current.remove(s[left])
                        
                        left = left+1
                    
                else:
                    
                    if right < len(s):
                        current.add(s[right])

                    if (right+1 - left + 1) > maxCount:
                        maxCount = right - left + 1
                    right = right + 1
        return maxCount
            





        