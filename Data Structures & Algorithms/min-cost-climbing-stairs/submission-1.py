class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        answer = [0] * len(cost)
        answer[-1] = cost[-1]
        if len(cost) == 1:
            return answer
        answer[len(cost) - 2] = cost[len(cost) -2]
        index = len(cost) -3
        while index > -1:
            answer[index] = cost[index] + min(answer[index+1], answer[index+2])
            index -= 1
        return min(answer[0], answer[1])





    