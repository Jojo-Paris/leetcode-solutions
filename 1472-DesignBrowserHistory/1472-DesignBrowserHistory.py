        self.history.append(url)

    def back(self, steps: int) -> str:

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.future) > 0:


# Your BrowserHistory object will be instantiated and called as such:
        while steps > 0 and len(self.history) > 1:
            self.future.append(self.history.pop())
        self.future = []
            steps -= 1
        return self.history[-1]
            self.history.append(self.future.pop())
# obj = BrowserHistory(homepage)
            steps -= 1
        
        return self.history[-1]
        self.future = []

    def visit(self, url: str) -> None:

    def __init__(self, homepage: str):
        self.history = [homepage]
class BrowserHistory:
[
