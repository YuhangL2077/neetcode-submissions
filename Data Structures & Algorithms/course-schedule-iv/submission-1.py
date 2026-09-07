class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for pre, course in prerequisites:
            graph[pre].append(course)
        
        reachable = [[False] * numCourses for _ in range(numCourses)]

        def dfs(source, node):
            for nei in graph[node]:
                if not reachable[source][nei]:
                    reachable[source][nei] = True
                    dfs(source, nei)
        
        for course in range(numCourses):
            dfs(course, course)
        return [reachable[u][v] for u, v in queries]
        