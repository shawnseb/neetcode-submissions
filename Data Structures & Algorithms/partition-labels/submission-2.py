class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        size = 0
        lasts = dict()
        index = 0
        for ch in s:
            lasts[ch] = index
            index += 1
        answer = []
        result = 0
        def getLastInWindow(start: int, end: int) ->int:
            for i in range(start, end + 1):
                if lasts[s[i]] > end:
                    return getLastInWindow(i+1, lasts[s[i]])
            return end+1
        while result != len(s):
            result = getLastInWindow(result, lasts[s[result]])
            if len(answer) >0:
                answer.append(result)
            else: 
                answer.append(result)
        
        for i in range(len(answer)-1, 0, -1):
            answer[i] = answer[i] - answer[i-1]

        return answer

    
                




        
            
        