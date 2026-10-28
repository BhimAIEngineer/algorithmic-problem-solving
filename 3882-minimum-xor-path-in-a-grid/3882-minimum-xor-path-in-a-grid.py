class Solution:

  def minCost(self, grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 << grid[0][0]

    for r in range(m):
      for c in range(n):
        if r == 0 and c == 0:
          continue

        current_mask = 0
        if r > 0:
          current_mask |= dp[r - 1][c]
        if c > 0:
          current_mask |= dp[r][c - 1]

        val = grid[r][c]
        new_mask = 0
        while current_mask:
          bit = current_mask & -current_mask
          v = bit.bit_length() - 1
          new_mask |= 1 << (v ^ val)
          current_mask ^= bit

        dp[r][c] = new_mask

    final_mask = dp[m - 1][n - 1]
    return (final_mask & -final_mask).bit_length() - 1