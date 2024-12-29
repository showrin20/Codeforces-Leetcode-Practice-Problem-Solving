class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parents, i):
            if parents[i] != i:
                parents[i] = find(parents, parents[i])
            return parents[i]
        
        def union(x, y, parents, size):
            root_x = find(parents, x)
            root_y = find(parents, y)
            if root_x != root_y:
                if size[root_x] < size[root_y]:
                    root_x, root_y = root_y, root_x
                parents[root_y] = root_x
                size[root_x] += size[root_y]
        
        def kruskals(n, edges):
            parents = [i for i in range(n)]
            size = [1] * n
            min_spanning_tree_cost = 0
            edges.sort(key=lambda x: x[2])
            for u, v, w in edges:
                if find(parents, u) != find(parents, v):
                    min_spanning_tree_cost += w
                    union(u, v, parents, size)
            return min_spanning_tree_cost
        
        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((i, j, w))
        
        return kruskals(n, edges)
