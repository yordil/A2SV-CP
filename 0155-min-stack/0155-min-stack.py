class MinStack:

    def __init__(self):
        self.stack = []
        self.min_tracer = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_tracer:
            idx , min_val = self.min_tracer[-1]  
            if val < min_val:
                self.min_tracer.append([len(self.stack)-1 , val])
        else:
            self.min_tracer.append([0 , val])
        

        


    def pop(self) -> None:
        self.stack.pop()

        idx , _ = self.min_tracer[-1]

        if idx == len(self.stack):
            self.min_tracer.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_tracer[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
