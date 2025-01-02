import heapq
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj_list = {i: [] for i in range(n)}
        for fromi, toi, pricei in flights:
            adj_list[fromi].append((toi, pricei))
        
        inf = math.inf
        visited = {}
        queue = []
        heapq.heappush(queue, (0, 0, src))
        
        while queue:
            current_dist, current_stop, current = heapq.heappop(queue)
            if current_stop > k + 1:
                continue
            if current == dst:
                return current_dist
            if current in visited and visited[current] <= current_stop:
                continue
            
            visited[current] = current_stop
            
            for nei, price in adj_list[current]:
                if nei not in visited or visited[nei] > current_stop + 1:
                    p=current_dist + price
                    p_stop=current_stop + 1
                    heapq.heappush(queue, (p, p_stop, nei))
        
        return -1
