import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hq = []
        for num in nums:
            heapq.heappush(hq, num)
        
        length = len(nums)
        while 1:
            num = heapq.heappop(hq)
            k += 1
            if k > length:
                return num
        return -1

