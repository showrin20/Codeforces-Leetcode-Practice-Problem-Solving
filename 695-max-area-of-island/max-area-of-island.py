class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_area = 0
        
        def dfs(r, c):
            area = 0
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                area = 1
                for dx, dy in direction:
                    nx, ny = r + dx, c + dy
                    area += dfs(nx, ny)
                return area
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area
