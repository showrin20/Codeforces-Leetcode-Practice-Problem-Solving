class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)

        def dfs(node,parent):
            if visited[node]:
                return True
            visited[node]=True

            for nei in adj_list[node]:
                if nei==parent:
                    continue
                if dfs(nei,node):
                    return True
            return False

        adj_list=[[] for i in range(n+1)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            visited=[False]*(n+1)
            if dfs(u,-1):
                return u,v
        i
