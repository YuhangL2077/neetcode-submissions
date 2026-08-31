from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #{1:[(2,1),(4,4)],2:[(3,1)],3:[(4,1)],4:[]}
        graph = defaultdict(list)
        dist = {node: float("inf") for node in range(1, n + 1)}
        dist[k] = 0
        min_heap = [(0, k)] #distance from src, src
        # build graph
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        while min_heap:
            curr_dist, node = heapq.heappop(min_heap)
            if curr_dist > dist[node]:
                continue
            for neighbor, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))
        if max(dist.values()) == float("inf"):
            return -1
        return max(dist.values())

        