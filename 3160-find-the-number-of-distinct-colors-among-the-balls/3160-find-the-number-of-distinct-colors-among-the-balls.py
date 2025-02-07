from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = Counter()
        balls = {}
        result = []
        for i, color in queries:
            prev_color = balls.get(i)
            if prev_color is not None:
                colors[prev_color] -= 1
                if colors[prev_color] == 0:
                    del colors[prev_color]

            balls[i] = color
            colors[color] += 1
            result.append(len(colors))
        return result


                
