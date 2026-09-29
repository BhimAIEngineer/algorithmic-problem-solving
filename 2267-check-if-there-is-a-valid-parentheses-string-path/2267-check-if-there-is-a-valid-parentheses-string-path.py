from collections import deque

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        visited = set([(0, 0, 1)])
        queue = deque([(0, 0, 1)])
        
        while queue:
            r, c, bal = queue.popleft()
            
            rem_steps = (m - 1 - r) + (n - 1 - c)
            if bal > rem_steps:
                continue
                
            for dr, dc in ((1, 0), (0, 1)):
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    nbal = bal + (1 if grid[nr][nc] == '(' else -1)
                    if nbal >= 0:
                        if nr == m - 1 and nc == n - 1 and nbal == 0:
                            return True
                        if (nr, nc, nbal) not in visited:
                            visited.add((nr, nc, nbal))
                            queue.append((nr, nc, nbal))
                            
        return False