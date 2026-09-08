import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        min_heap = []
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        heapq.heappush(min_heap, (0,0,0)) #diff, col, row 
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if (r, c) == (rows - 1, cols - 1):
                return effort
            if effort > dist[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_effort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        dist[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))

        return 0