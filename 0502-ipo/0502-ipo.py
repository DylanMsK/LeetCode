import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ## 시간 초과
        # hq = []
        # for idx, p in enumerate(profits):
        #     heapq.heappush(hq, (-p, idx))
        
        # for _ in range(k):
        #     temp = []
        #     while hq:
        #         profit, idx = heapq.heappop(hq)
        #         if capital[idx] <= w:
        #             w -= profit
        #             break
        #         else:
        #             temp.append((profit, idx))
            
        #     for profit, idx in temp:
        #         heapq.heappush(hq, (profit, idx))

        projects = sorted(zip(capital, profits), key=lambda x: x[0])

        profit_max_heap = []
        length = len(projects)
        idx = 0
        for _ in range(k):
            while idx < length and projects[idx][0] <= w:
                heapq.heappush(profit_max_heap, -projects[idx][1])
                idx += 1
            if not profit_max_heap:
                break
            w += -heapq.heappop(profit_max_heap)

        return w