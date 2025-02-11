import heapq

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        _max = 0
        while l <= r:
            area = (r - l) * min(height[l], height[r])
            _max = max(_max, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return _max

