from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digits = defaultdict(int) # {digit_sum: num}
        _max = -1
        for num in nums:
            digit_sum = self.digit_sum(num)
            prev_num = digits[digit_sum]
            if prev_num:
                _max = max(_max, prev_num + num)
                if num >= prev_num:
                    digits[digit_sum] = num
            else:
                digits[digit_sum] = num

        return _max

    def digit_sum(self, num):
        result = 0
        while num > 0:
            result += num % 10
            num //= 10
        return result