class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = [intervals.pop(0)]
        while intervals:
            start, end = intervals.pop(0)
            for i in range(len(merged)):
                s, e = merged[i]
                if start <= e:
                    merged[i][1] = max(end, e)
                    break
            else:
                merged.append([start, end])

        return merged