class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        nums = []
        for i in range(1, n+1):
            if n % i == 0:
                nums.append(i)
                if len(nums) == k:
                    return nums[-1]
        return -1