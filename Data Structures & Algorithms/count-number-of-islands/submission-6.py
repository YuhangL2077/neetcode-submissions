class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        islands = 0
        visited = set()
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    visited.add((r, c))
                    q.append((r, c))
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == "1":
                                visited.add((nr, nc))
                                q.append((nr, nc))


        return islands


             

