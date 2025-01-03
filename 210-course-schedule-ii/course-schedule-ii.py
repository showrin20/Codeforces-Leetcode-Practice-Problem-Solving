class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
        
        visited = [0] * numCourses
        stack = []
        cycle_detected = False

        def dfs(node):
            nonlocal cycle_detected
            if cycle_detected:
                return
            if visited[node]== -1:
                cycle_detected = True
                return

            if visited[node]==1:
                return
            visited[node]= -1
            for neighbour in adj_list[node]:
                dfs(neighbour)

            visited[node]=1
            stack.append(node)
        
            
        for node in range(numCourses):
            if not visited[node]:
                dfs(node)

        return stack[::-1] if not cycle_detected else []
