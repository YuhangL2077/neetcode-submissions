class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(r, c):
            longest = 1
            if (r, c) in memo:
                return memo[(r, c)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                    longest = max(longest, 1 + dfs(nr, nc))

            memo[(r, c)] = longest
            return longest

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = max(ans, dfs(r, c))

        return ans
