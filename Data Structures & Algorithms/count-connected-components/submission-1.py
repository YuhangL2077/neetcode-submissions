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
#如果只遍历edges会漏掉完全没有出现在 edges 里的 isolated node
        for u, v in edges:
            union(u, v)

        for i in range(n):
            root.add(find(i))

        return len(root)


        