from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        visited = [0] * numCourses
        is_possible = True

        for pre in prerequisites:
            graph[pre[1]].append(pre[0])

        def dfs(node):
            nonlocal is_possible
            if visited[node] == 1:
                is_possible = False
                return
            if visited[node] == 2:
                return

            visited[node] = 1
            for neighbour in graph[node]:
                dfs(neighbour)

            visited[node] = 2

        for course in range(numCourses):
            if visited[course] == 0:
                dfs(course)

        return is_possible