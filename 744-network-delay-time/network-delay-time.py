import heapq
from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj_list[u].append((v, w))
        
        dist = [inf] * (n + 1)
        dist[k] = 0
        queue = [(0, k)]
        
        while queue:
            current_dist, current = heapq.heappop(queue)
            if current_dist > dist[current]:
                continue
            for v, w in adj_list[current]:
                new_dist = current_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(queue, (new_dist, v))
        
        max_dist = max(dist[1:])
        return -1 if max_dist == inf else max_dist
