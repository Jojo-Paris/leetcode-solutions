class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()


        while self.requests[0] < t - 3000: 
            self.requests.popleft()
            print(self.requests)
        return len(self.requests)
            
# param_1 = obj.ping(t)
[
