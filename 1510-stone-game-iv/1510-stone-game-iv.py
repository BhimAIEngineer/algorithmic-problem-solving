class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]
        for i in range(1, n + 1):
            dp.append(any(not dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)))
        return dp[n]