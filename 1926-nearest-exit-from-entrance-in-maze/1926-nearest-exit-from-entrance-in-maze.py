class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        count = [[float("inf") for _ in range(n)] for _ in range(m)]
        count[entrance[0]][entrance[1]] = 0
        currents = [entrance]
        dy = [1, -1, 0, 0]
        dx = [0, 0, -1, 1]
        _min = float("inf")
        flag = False

        while currents:
            y, x = currents.pop(0)
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny < 0 or ny >= m or nx < 0 or nx >= n:  # 미로를 탈출하면
                    if count[y][x] == 0:
                        continue
                    _min = min(_min, count[y][x])
                    flag = True
                    break

                if maze[ny][nx] == "+":  # 벽을 만나면
                    continue

                if count[y][x] + 1 < count[ny][nx]:  # 과거 방문보다 빠르면
                    count[ny][nx] = count[y][x] + 1
                    currents.append([ny, nx])
                    continue
                
        return _min if flag else -1