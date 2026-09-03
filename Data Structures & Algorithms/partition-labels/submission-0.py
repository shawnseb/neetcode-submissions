class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        lastindices = dict()
        index = 0
        for ch in s:
            lastindices[ch] = index
            index += 1
        answer = []
        result = 0
        def getLastInWindow(string: str, lasts: dict, start: int, end: int) ->int:
            for i in range(start, end + 1):
                if lasts[string[i]] > end:
                    return getLastInWindow(string, lasts, i+1, lasts[string[i]])
            return end+1
        while result != len(s):
            result = getLastInWindow(s, lastindices, result, lastindices[s[result]])
            if len(answer) >0:
                answer.append(result)
            else: 
                answer.append(result)
        
        for i in range(len(answer)-1, 0, -1):
            answer[i] = answer[i] - answer[i-1]

        return answer

    
                




        
            
        