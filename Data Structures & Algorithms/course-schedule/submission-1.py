from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build graph and initianize indegree
        graph = [[] for _ in range(numCourses)]

        indegree = [0] * numCourses
        #[0, 0, 0, 0]

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        print(graph)
        # [[3], [0], [0], []]
        print(indegree)
        # [2, 0, 0, 1]

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            course = q.popleft()
            completed += 1

            for nei in graph[course]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return completed == numCourses