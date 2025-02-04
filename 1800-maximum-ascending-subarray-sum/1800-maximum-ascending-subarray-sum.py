class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        _max = nums[0]
        _sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                _sum += nums[i]
                _max = max(_max, _sum)
            else:
                _sum = nums[i]

        return _max
        