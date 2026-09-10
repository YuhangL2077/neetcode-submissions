class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        heap = []
        dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        heap.append((grid[0][0],0,0)) #time, r, c
        dist[0][0] = grid[0][0]
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap:
            curr_time, r, c = heapq.heappop(heap)
            if curr_time > dist[r][c]:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
       

                    new_time = max(curr_time, grid[nr][nc])
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(heap, (new_time, nr, nc))

        return dist[rows - 1][cols - 1] if dist[rows - 1][cols - 1] != float("inf") else grid[0][0]
        