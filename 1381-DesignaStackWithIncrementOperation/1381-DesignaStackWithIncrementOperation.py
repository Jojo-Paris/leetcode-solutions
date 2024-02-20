class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:   

    def pop(self) -> int:
        if self.stack: return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(len(self.stack)):


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
        self.maxSize = maxSize
        
            self.stack.append(x)
            if i == k: break
            self.stack[i] += val
        else: return -1
# obj.increment(k,val)
[
