class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for c in s:
            if c != "*":
                result.append(c)
            else:
                result.pop()
        return "".join(result)
