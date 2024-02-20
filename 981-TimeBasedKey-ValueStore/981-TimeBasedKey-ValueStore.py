
    def get(self, key: str, timestamp: int) -> str:
        self.arr[key].append([value, timestamp])
            self.arr[key] = []
        

        while l <= r:
            mid = (l + r) // 2
            val = self.arr[key][mid][1]
            if val < timestamp:
        temp = ''
                l = mid + 1
            else:
                r = mid - 1
            if val == timestamp: return self.arr[key][mid][0]


            
            temp = self.arr[key][mid][0]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
    def __init__(self):
        self.arr = {}

        values = self.arr.get(key, [])
        l, r = 0, len(values) - 1
        
[
