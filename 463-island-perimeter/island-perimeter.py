class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 1
            if (r, c) in visit:
                return 0

            visit.add((r, c))
            current_perimeter = 0
            for dx, dy in directions:
                n_r, n_c = r + dx, c + dy
                current_perimeter += dfs(n_r, n_c)
            return current_perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i, j) 
        return 0
