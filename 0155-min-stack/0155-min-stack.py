class MinStack:

    def __init__(self):
        self.stack = []
        self.Min = []

    def push(self, val: int) -> None:
            self.stack.append(val)
            val = min(val , val if not self.Min else self.Min[-1])
            self.Min.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.Min.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.Min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()