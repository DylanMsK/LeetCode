class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        _max = 1
        increasing_nums = nums[:1]
        decreasing_nums = nums[:1]
        for i in range(len(nums)):
            n = nums[i]
            if n > increasing_nums[-1]:
                increasing_nums.append(n)
            else:
                increasing_nums = [n]
            
            if n < decreasing_nums[-1]:
                decreasing_nums.append(n)
            else:
                decreasing_nums = [n]

            _max = max(_max, len(increasing_nums), len(decreasing_nums))
        return _max


        