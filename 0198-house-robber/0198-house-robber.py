class Solution:
    def rob(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            if idx == 0:
                continue
            elif idx == 1:
                nums[idx] = max(nums[:idx+1])
            else:
                nums[idx] = max(nums[idx-1], nums[idx-2] + nums[idx])
        return nums[-1]