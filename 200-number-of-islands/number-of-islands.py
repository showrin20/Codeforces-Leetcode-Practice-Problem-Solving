from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island_count += 1 
                    bfs(r, c) 

        return island_count
