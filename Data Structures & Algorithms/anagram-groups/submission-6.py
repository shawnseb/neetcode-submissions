import copy
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        for i, word in enumerate(strs):
            bank = [0] * 26
            for char in word:
                offset = ord(char) - ord('a')
                bank[offset]+=1
            key = tuple(bank)
            if key in seen:
                seen[key].append(word)
            else:
                seen[key] = [word]
        answer = []
        for i in seen:
            answer.append(seen[i])
        return answer
            
        