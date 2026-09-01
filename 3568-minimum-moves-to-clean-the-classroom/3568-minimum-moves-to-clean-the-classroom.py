from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        R, C = len(classroom), len(classroom[0])
        
        litters = []
        sr, sc = -1, -1
        
        for r in range(R):
            for c in range(C):
                ch = classroom[r][c]
                if ch == 'S':
                    sr, sc = r, c
                elif ch == 'L':
                    litters.append((r, c))
                    
        k = len(litters)
        target_mask = (1 << k) - 1
        
        if target_mask == 0:
            return 0
            
        litter_map = {pos: i for i, pos in enumerate(litters)}
        
        grid = [[-3] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                ch = classroom[r][c]
                if ch == 'X':
                    grid[r][c] = -2
                elif ch == 'R':
                    grid[r][c] = -1
                elif ch == 'L':
                    grid[r][c] = litter_map[(r, c)]
                else:
                    grid[r][c] = -3
                    
        best_energy = [[[-1] * (1 << k) for _ in range(C)] for _ in range(R)]
        best_energy[sr][sc][0] = energy
        
        queue = deque([(sr, sc, 0, energy, 0)])
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
        
        while queue:
            r, c, mask, e, dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    cell_code = grid[nr][nc]
                    if cell_code == -2:
                        continue
                        
                    ne = e - 1
                    if ne < 0:
                        continue
                        
                    nmask = mask
                    if cell_code >= 0:
                        nmask = mask | (1 << cell_code)
                        
                    if nmask == target_mask:
                        return dist + 1
                        
                    if cell_code == -1:
                        ne = energy
                        
                    if ne == 0:
                        continue
                        
                    if ne <= best_energy[nr][nc][nmask]:
                        continue
                        
                    best_energy[nr][nc][nmask] = ne
                    queue.append((nr, nc, nmask, ne, dist + 1))
                    
        return -1