from typing import List
from collections import deque

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(start_r, start_c):
            queue = deque([(start_r, start_c, None)])  
            visited.add((start_r, start_c))
            
            while queue:
                row, col, parent = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == grid[row][col]:
                        if (new_r, new_c) not in visited:
                            queue.append((new_r, new_c, (row, col)))
                            visited.add((new_r, new_c))
                        elif (new_r, new_c) != parent:  
                            return True
            return False
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    if bfs(r, c):  
                        return True
        
        return False
