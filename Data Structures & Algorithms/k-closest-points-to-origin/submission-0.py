import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        world = dict()
        distances = []
        index = 0
        for i in points:
            dist = math.sqrt(i[0] ** 2 + i[1] ** 2)
            if dist not in distances:
                world[dist] = [i]
                print("hey")

            else:
                segment = world[dist]
                segment.append(i)
                world[dist] = segment
            distances.append(dist)
        heapq.heapify(distances)
        answers = []
        print(distances)
        for i in range (k):
            answer = world[heapq.heappop(distances)]
            small = -1
            if len(answer) > 1:
                small = answer.pop()
            else:
                small = answer[0]

            answers.append(small)
        
        return answers
        

        