class RecentCounter:

    def __init__(self):
        self.calls = []

    def ping(self, t: int) -> int:
        self.calls.append(t)
        # for i in range(len(self.calls)):
        #     if self.calls[i] >= t - 3000:
        #         self.calls = self.calls[i:]
        #         break
        while self.calls:
            if self.calls[0] >= t - 3000:
                break
            self.calls.pop(0)
        return len(self.calls)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)