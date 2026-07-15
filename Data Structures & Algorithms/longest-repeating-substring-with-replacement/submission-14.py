class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # A dictionary to count the frequencies of characters in our current window
        count = {}
        best_answer = 0
        
        left = 0
        max_frequency = 0
        
        for right in range(len(s)):
            # Add the rightmost character to our window count
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Keep track of the highest frequency of a single character in the window
            max_frequency = max(max_frequency, count[s[right]])
            
            # The current window size is (right - left + 1).
            # If the window size minus the most frequent character is greater than k, 
            # it means we don't have enough replacements to make the window valid.
            while (right - left + 1) - max_frequency > k:
                # Shrink the window from the left until it's valid again
                count[s[left]] -= 1
                left += 1
                
            # Update our best answer if this valid window is the largest we've seen
            best_answer = max(best_answer, right - left + 1)
            
        return best_answer
        
    def findGaps(self, s : str, start: int)-> dict():
        print(start)
        tip = s[start]
        i = 0
        last = 0
        gap = 0
        gaps = dict()
        tips = dict()
        if start > 0:
            gaps[0] = start

        lastGap = -1
        lastTipStart=0
        tipLength = 0
        for letter in s:
            print(lastGap)
            if letter == tip:
                print('c')
                last = i
                gap = 0
                if tipLength == 0:
                    lastTipStart = i
                tipLength = tipLength+1
                tips[lastTipStart] = tipLength
                
            if letter!= tip:
                print('g')
                if gap == 0:
                    lastGap = i
                gap = gap + 1
                gaps[lastGap] = gap

                if tipLength > 0:
                    tipLength = 0

            i = i + 1
        return tips
        
    def fillGaps(self, gaps: dict(), k:int, s: str)->int:
        if not gaps:
            return 0
            
        if k == 0:
            return max(gaps.values())
            
        while k > 0:
            substance = sorted(gaps)
            
            if len(substance) <= 1:
                return min(len(s), gaps[substance[0]] + k)
            
            maxIndex = -1
            iteration_max = 0
            i = 0
            while i < len(substance):
                current_key = substance[i]
                if i < len(substance) - 1:
                    gap = substance[i+1] - (current_key + gaps[current_key])
                    if k >= gap:
                        total = substance[i+1] + gaps[substance[i+1]] - current_key
                        if iteration_max <= total:
                            iteration_max = total
                            maxIndex = i
                i = i + 1
                
            if maxIndex == -1:
                return min(len(s), max(gaps.values()) + k)
                
            hey = substance[maxIndex]
            ho = substance[maxIndex+1]
            k = k - (ho - (hey + gaps[hey]))
            gaps.pop(hey, None)
            gaps.pop(ho, None)
            gaps[hey] = iteration_max

        return min(len(s), max(gaps.values()) + k)
        
    class Openings:
        def __init__(self, index: List[int], length: List[int]):
            self.index = index
            self.length = length
            return