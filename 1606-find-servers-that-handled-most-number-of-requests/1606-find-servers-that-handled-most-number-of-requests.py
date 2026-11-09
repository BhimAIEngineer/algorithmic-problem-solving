import heapq
from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        available = SortedList(range(k))
        busy = []
        req_count = [0] * k
        
        for i, (arr, dur) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= arr:
                _, s_id = heapq.heappop(busy)
                available.add(s_id)
                
            if not available:
                continue
                
            preferred = i % k
            idx = available.bisect_left(preferred)
            if idx == len(available):
                idx = 0
                
            s_id = available[idx]
            available.pop(idx)
            heapq.heappush(busy, (arr + dur, s_id))
            req_count[s_id] += 1
            
        max_req = max(req_count)
        return [i for i, c in enumerate(req_count) if c == max_req]