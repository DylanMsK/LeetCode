class MinStack:

    def __init__(self):
        self._min = float("inf") 
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self._min = min(self._min, val)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self._min:
            if self.stack:
                self._min = min(self.stack)
            else:
                self._min = float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()