class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = COLS = len(grid)
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque()
        q.append((0,0))
        visited = set((0,0))
        step = 1
        if grid[0][0] == 1 or grid[ROWS - 1][COLS - 1] == 1:
            return -1

        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                if (r, c) == (ROWS - 1, COLS - 1):
                            return step
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            step += 1

        return -1

                
        