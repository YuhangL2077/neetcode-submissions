class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        # dist[node][edges_used]
        dist[src][0] = 0
        for u, v, price in flights:
            graph[u].append((v, price))

        min_heap = []
        min_heap.append((0, src, 0)) #cost, src, edges used
        
        while min_heap:
            cost, node, edges_used = heapq.heappop(min_heap)
            # stale check
            if cost > dist[node][edges_used]:
                continue
            # target check
            if node == dst:
                return cost

            if edges_used == k + 1:
                continue

            for nei, price in graph[node]:
                new_cost = cost + price
                new_edges = edges_used + 1

                if new_cost < dist[nei][new_edges]:
                    dist[nei][new_edges] = new_cost
                    heapq.heappush(min_heap, (new_cost, nei, new_edges))

        return -1
        