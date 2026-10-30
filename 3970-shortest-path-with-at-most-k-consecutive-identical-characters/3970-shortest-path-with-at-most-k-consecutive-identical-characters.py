import heapq

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        
        pq = [(0, 0, 1)]
        
        while pq:
            d, u, count = heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            if d > dist[u][count]:
                continue
                
            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    next_count = count + 1
                else:
                    next_count = 1
                    
                if next_count <= k:
                    if d + w < dist[v][next_count]:
                        dist[v][next_count] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))
                        
        return -1