class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                top = stack.pop()
                result[top] = idx - top
            stack.append(idx)
        return result

