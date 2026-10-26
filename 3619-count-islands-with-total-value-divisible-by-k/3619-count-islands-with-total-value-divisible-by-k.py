from collections import deque


class Solution:

  def countIslands(self, grid: list[list[int]], k: int) -> int:
    if not grid or not grid[0]:
      return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] > 0:
          current_island_sum = 0
          q = deque([(r, c)])
          current_island_sum += grid[r][c]
          grid[r][c] = 0

          while q:
            curr_r, curr_c = q.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
              nr, nc = curr_r + dr, curr_c + dc
              if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                current_island_sum += grid[nr][nc]
                grid[nr][nc] = 0
                q.append((nr, nc))

          if current_island_sum % k == 0:
            count += 1

    return count