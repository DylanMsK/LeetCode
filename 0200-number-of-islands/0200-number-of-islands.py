class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    self.dfs(grid, x, y)
                    cnt += 1
        return cnt
    
    def dfs(self, grid: List[List[str]], x: int, y: int):
        m, n = len(grid), len(grid[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        stack = [(x, y)]
        while stack:
            x, y = stack.pop()
            grid[y][x] = "0"
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[ny][nx] == '1':
                    stack.append((nx, ny))


            



        