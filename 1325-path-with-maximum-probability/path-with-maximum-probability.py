import heapq

class Solution:
    def maxProbability(self, n: int, edges: list, succProb: list, start: int, end: int) -> float:
        adj_lst = {i: [] for i in range(n)}
        for i in range(len(edges)):
            u, v = edges[i]
            adj_lst[u].append((v, succProb[i]))
            adj_lst[v].append((u, succProb[i]))


        dist = [0.0] * n
        queue = []
        heapq.heappush(queue, (-1, start))

        while queue:
            current_prob, current = heapq.heappop(queue)
            current_prob = -current_prob
            if current == end:
                return current_prob
            for nei, prob in adj_lst[current]:
                new_prob = current_prob * prob
                if new_prob > dist[nei]:
                    dist[nei] = new_prob
                    heapq.heappush(queue, (-new_prob, nei))

        return 0.0
