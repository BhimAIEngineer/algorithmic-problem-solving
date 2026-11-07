import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        n = len(servers)
        m = len(tasks)
        
        free_servers = []
        for i in range(n):
            heapq.heappush(free_servers, (servers[i], i))
            
        busy_servers = []
        ans = [-1] * m
        current_time = 0
        
        for j in range(m):
            current_time = max(current_time, j)
            
            while busy_servers and busy_servers[0][0] <= current_time:
                _, server_weight, server_index = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (server_weight, server_index))
                
            if not free_servers:
                current_time = busy_servers[0][0]
                while busy_servers and busy_servers[0][0] <= current_time:
                    _, server_weight, server_index = heapq.heappop(busy_servers)
                    heapq.heappush(free_servers, (server_weight, server_index))
                    
            server_weight, server_index = heapq.heappop(free_servers)
            ans[j] = server_index
            heapq.heappush(busy_servers, (current_time + tasks[j], server_weight, server_index))
            
        return ans