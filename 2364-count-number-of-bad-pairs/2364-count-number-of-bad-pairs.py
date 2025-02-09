from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        good = 0
        for i, num in enumerate(nums):
            good += counter[num-i]
            counter[num-i] += 1
        
        length = len(nums)
        total = (length * (length - 1)) // 2
        return total - good