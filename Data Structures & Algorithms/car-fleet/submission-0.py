class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        map = dict()
        for pos, speed in zip(position, speed):
            map[pos] = speed
        position.sort()
        initial = 0
        fleets = 0
        while len(position) != 0:
            initial = (target - position[-1]) / map[position[-1]]
            position.pop()
            fleets += 1
            time = 0
            
            while initial >= time and len(position) != 0:
                time = (target - position[-1]) / map[position[-1]]
                if time <= initial:
                    position.pop()
        return fleets




        
        