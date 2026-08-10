class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        world = dict()
        for task in tasks:
            if task not in world:
                world[task] = 1
            else:
                world[task] += 1
        print(world)
        prev = ""
        prevCycle = -1
        cycles = 0
        arr = []
        for task in world:
            arr.append(task)
        arr.sort(key=lambda task: world[task], reverse=True)
        
        print(arr)
        switch = False
        while len(arr) > n: 
            for task in arr:
                print("happened")
                if world[task] - 1 == 0:
                    print(task)
                    arr.remove(task)
                    cycles += 1
                    prev = task 
                    break
                else:
                    print(task)
                    world[task] -= 1
                    cycles += 1
                    prev = task
        print(cycles)
        if len(arr) == 0:
            return cycles
        cycles += (n +1) * (world[arr[0]] - 1)
        print(cycles)
        index = 0
        while index < len(arr) and world[arr[0]] == world[arr[index]]:
            index += 1
        print(index)
        
        
        cycles += index

        return cycles
                
                

        