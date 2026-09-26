class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary = dict()
        for i in s:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
        for i in t:
            if i not in dictionary:
                return False
            if dictionary[i] == 0:
                return False
            dictionary[i]-=1
        return True
        
