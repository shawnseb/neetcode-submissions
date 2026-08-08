class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        def getRemainder(num: int) -> int:
            comp = 0
            while(2 ** comp<= num):
                comp+= 1
            return num - 2 ** (comp - 1)
        bucket = n
        answer = 0
        while bucket != 0:
            bucket = getRemainder(bucket)
            answer += 1
        return answer




        