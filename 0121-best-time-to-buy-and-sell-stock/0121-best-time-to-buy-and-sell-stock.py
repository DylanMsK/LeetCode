class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        _max = 0
        for price in prices:
            if price < _min:
                _min = price
            else:
                _max = max(_max, price - _min)
        return _max
