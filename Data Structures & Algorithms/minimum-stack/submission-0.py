class MinStack:

    def __init__(self):
        self.stack = []
        self.min =None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.min = val
        if val < self.min:
            self.min = val

        

    def pop(self) -> None:
        self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        min = self.min
        if self.min not in self.stack:
            min = self.stack[0]
            for item in self.stack:
                if item < min:
                    min = item
        return min
        
