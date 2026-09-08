from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        dist = [float("inf") for i in range(n + 1)]
        min_heap = [(0, k)]
        dist[k] = 0
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)

            if curr_dist > dist[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
        
        max_distance = max(dist[1:])
        if max_distance != float("inf"):
            return max_distance
        return -1

            

        