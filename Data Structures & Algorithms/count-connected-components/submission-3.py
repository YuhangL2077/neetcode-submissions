class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * (n)
        ans = 0
        root = set()
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
#最好写法：直接维护 component count，它更漂亮，而且不需要最后再遍历一遍。
        components = n
        for u, v in edges:
            if union(u, v):
                components -= 1

        return components

#Initially every node is its own component. Every successful union merges two components, so the number of components decreases by one.

        