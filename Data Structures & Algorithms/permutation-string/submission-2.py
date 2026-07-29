class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        short = s1
        long = s2
        permutation = dict()
        
        for i in short:
            if i not in permutation:
                permutation[i] = 1
            else: 
                permutation[i] = permutation[i] + 1
        copy = permutation.copy()
        
        for i in range(0, len(long) - len(short) + 1):

            copy = permutation.copy()
            for j in range(i, i + len(short)):
                
                letter = long[j]
                if letter not in copy:
                    break
                elif copy[letter] == 0:
                    break
                else:
                    copy[letter] = copy[letter] - 1
                if j == len(short) -1 + i:
                    return True
                

        return False
        