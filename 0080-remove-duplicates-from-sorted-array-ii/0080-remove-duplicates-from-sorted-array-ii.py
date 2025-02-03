class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        k = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                if nums[k] == nums[k-1]:
                    continue
                else:
                    k += 1
                    nums[k] = nums[i]
            else:
                if k < i:
                    k += 1
                    nums[k] = nums[i]
        return k + 1

