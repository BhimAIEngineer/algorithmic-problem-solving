class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [0] * n
        dp[0] = 1 << 1

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    continue

                prev_mask = (dp[c] if r > 0 else 0) | (dp[c - 1] if c > 0 else 0)

                if grid[r][c] == '(':
                    dp[c] = prev_mask << 1
                else:
                    dp[c] = prev_mask >> 1

        return bool(dp[-1] & 1)