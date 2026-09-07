class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        
        q = deque([0])
        visited = set()
        visited.add(0)


        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        while q:
            node = q.popleft()
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return True if len(visited) == n else False
            
        