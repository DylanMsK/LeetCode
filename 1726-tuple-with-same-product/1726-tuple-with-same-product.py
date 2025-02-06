from collections import Counter

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = Counter()
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                ans = nums[i] * nums[j]
                result += cnt[ans]
                cnt[ans] += 1
        return result * 8