
    def get(self, key: str, timestamp: int) -> str:

        while l <= r:
            mid = (l + r) // 2
            val = self.arr[key][mid][1]
            if val <= timestamp:
        temp = ''
                l = mid + 1
            else:
                r = mid - 1

            
            
        values = self.arr.get(key, [])
        l, r = 0, len(values) - 1
        
        return temp

        self.arr[key].append([value, timestamp])
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.arr:
            self.arr[key] = []
                temp = self.arr[key][mid][0]


[
