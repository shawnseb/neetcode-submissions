class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answers =  dict()
        index = 0
        for num in numbers:
            if target - num in answers:
                return [answers[target - num] + 1, index + 1]
            answers[num] = index
            index += 1
        return [-1]