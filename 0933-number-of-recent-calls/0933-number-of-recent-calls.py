class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        self.calls = [i for i in self.calls if i >= t - 3000]
        return len(self.calls)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)