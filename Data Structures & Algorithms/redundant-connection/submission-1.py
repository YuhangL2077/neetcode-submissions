class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)
        
        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x


        def union(x, y):
            px = find(x)
            py = find(y)
            if px == py:
                return False

            if rank[px] < rank[py]:
                px, py = py, px

            parent[py] = px
            rank[px] += rank[py]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]













