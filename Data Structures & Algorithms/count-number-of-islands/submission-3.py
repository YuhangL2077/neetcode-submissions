from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island += 1
                    visited.add((r, c))
                    q.append((r, c))
                    while q:
                        rr, cc = q.popleft()
                        for dr, dc in directions:
                            nr, nc = rr + dr, cc + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                q.append((nr, nc))
        return island



        