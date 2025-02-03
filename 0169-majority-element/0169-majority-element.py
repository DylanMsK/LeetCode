class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = {}
        for n in nums:
            if result.get(n):
                result[n] += 1
            else:
                result[n] = 1
        
        max_n = 0
        max_count = 0
        for n, count in result.items():
            if count > max_count:
                max_count = count
                max_n = n

        return max_n