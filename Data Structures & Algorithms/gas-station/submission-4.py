class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def completeCircuitTry(index: int) -> (bool, int):
            gasLeft = 0
            start = index
            run = True
            while gasLeft >= 0 and (index!=start or run) :
                run = False
                gasLeft+=gas[index]
                gasLeft-=cost[index]
                index+=1
                if index == len(gas):
                    index = 0
                
              
            if gasLeft < 0:
               
                return False, index
                
            else:
                print(f"End {gasLeft}")
                return True, start
        
        start = 0
        visited = set()
        for i in range (len(gas)):
            if start in visited:
                return -1
            
            boolean, index = completeCircuitTry(start)
            if boolean and index == start:
                return index
            visited.add(start)
            start = index
        return -1
            
            
            

        
        