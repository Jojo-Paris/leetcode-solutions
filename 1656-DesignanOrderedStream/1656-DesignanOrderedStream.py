class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
        self.ptr = 0
        self.arr[idKey] = value
        if idKey != self.ptr:
            return []
        
        while self.ptr < len(self.arr) and self.arr[self.ptr]: self.ptr += 1
        return self.arr[idKey:self.ptr]
# param_1 = obj.insert(idKey,value)
[
