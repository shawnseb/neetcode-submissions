import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        def getRemainder(num:int)->int:
            result = math.log(num, 2)
            return num - 2 ** (int(result))
        answer = [0]
        for i in range(1, n + 1):
            output = 0
            bucket = i
            while bucket != 0:
                bucket &= bucket - 1
                output += 1
            answer.append(output)
        return answer


        