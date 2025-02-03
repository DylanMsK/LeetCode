class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        origin = nums[:]
        k %= l
        for i in range(l):
            if i + k >= l:
                nums[i+k-l] = origin[i]
            else:
                nums[i+k] = origin[i]