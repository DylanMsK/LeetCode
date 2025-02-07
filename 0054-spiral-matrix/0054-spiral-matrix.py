class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        result = []
        x, y, d = -1, 0, 0
        while len(result) != m * n:
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and matrix[ny][nx] is not False:
                result.append(matrix[ny][nx])
                matrix[ny][nx] = False
                x, y = nx, ny
            else:
                d += 1
                d %= 4
        
        return result
                
