class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tset = {}
        for c in s:
            tset[c] = tset.get(c,0) + 1;
        for c in t:
            if c not in tset or tset[c] == 0 :
                return False
            else:
                tset[c]= tset[c]-1
        
        return True
    