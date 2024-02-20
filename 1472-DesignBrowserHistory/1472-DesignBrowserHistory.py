
    def visit(self, url: str) -> None:
        self.history.append(url)

    def back(self, steps: int) -> str:

    def forward(self, steps: int) -> str:
        while steps > 0 and len(self.future) > 0:


# Your BrowserHistory object will be instantiated and called as such:
        while steps > 0 and len(self.history) > 1:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.future = []
            self.future.append(self.history.pop())
        self.future = []
            steps -= 1
        return self.history[-1]
class BrowserHistory:

            self.history.append(self.future.pop())
# obj = BrowserHistory(homepage)
            steps -= 1
        
        return self.history[-1]
[
