class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda l: l[1])
        indexed_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        ans = [0] * len(queries)
        count = [0] * (n + 1)
        active_servers = 0
        
        log_idx = 0
        remove_idx = 0
        
        for orig_idx, q in indexed_queries:
            start = q - x
            while log_idx < len(logs) and logs[log_idx][1] <= q:
                server, t = logs[log_idx]
                if count[server] == 0:
                    active_servers += 1
                count[server] += 1
                log_idx += 1
                
            while remove_idx < len(logs) and logs[remove_idx][1] < start:
                server, t = logs[remove_idx]
                count[server] -= 1
                if count[server] == 0:
                    active_servers -= 1
                remove_idx += 1
                
            ans[orig_idx] = n - active_servers
            
        return ans